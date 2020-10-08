from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Import django-registration-redux
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Import models
from booking_app.models import Building, Room, UserProfile, Event

# Import forms
from booking_app.forms import UserForm, UserProfileForm

from datetime import datetime
from django.views import View
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

#from django.http import JsonResponse
#import json


# Views:
# Index page view
class IndexView(View):
    def get(self, request):
        building_list = Building.objects.order_by('-likes')[:5]
        
        context_dict = {}
        context_dict['buildings'] = building_list
        return render(request, 'booking_app/index.html', context=context_dict)
        
# Show buildings
class ShowBuildingView(View):
    def create_context_dict(self, building_name_slug):
        context_dict = {}

        try:
            building = Building.objects.get(slug=building_name_slug)
            rooms = Room.objects.filter(building=building).order_by('-views')

            context_dict['rooms'] = rooms
            context_dict['building'] = building

        except Building.DoesNotExist:
            context_dict['rooms'] = None
            context_dict['building'] = None

        return context_dict

    def get(self, request, building_name_slug):
        context_dict = self.create_context_dict(building_name_slug)
        return render(request, 'booking_app/building.html', context_dict)

class ShowRoomView(View):
    def create_context_dict(self, room_name_slug):
        context_dict = {}

        try:
            room = Room.objects.get(slug=room_name_slug)
            context_dict['room'] = room
            
        except Room.DoesNotExist:
            context_dict['room'] = None

        return context_dict

    def get(self, request, room_name_slug, building_name_slug):
        context_dict = self.create_context_dict(room_name_slug)
        return render(request, 'booking_app/room.html', context_dict)


# Register view

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
        
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'booking_app/register.html',context = {'user_form': user_form,'profile_form': profile_form,'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('booking_app:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

# like building
class LikeBuildingView(View):
    @method_decorator(login_required)
    def get(self, request):
        building_id = request.GET['building_id']

        try:
            building = Building.objects.get(id=int(building_id))
        except Building.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-2)
        
        building.likes = building.likes + 1
        building.save()

        return HttpResponse(building.likes)


class AddEventView(View):
    @method_decorator(login_required)
    def get(self, request):
        title = request.GET['title']
        start = request.GET['start']
        end = request.GET['end']
        
        e = Event.objects.get_or_create(title=title,start=start,end=end)

        return HttpResponse(True)


# Register user profile
class RegisterProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = UserProfileForm()
        context_dict = {'form': form}
        return render(request, 'booking_app/profile_registration.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('booking_app:index'))
        else:
            print(form.errors)
        
        context_dict = {'form': form}
        return render(request, 'booking_app/profile_registration.html', context_dict)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'website': user_profile.website,
                                'picture': user_profile.picture})
        
        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('booking_app:index'))
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'booking_app/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('booking_app:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('booking_app:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'booking_app/profile.html', context_dict)

# Ajax tests
class Test(View):
    @method_decorator(login_required)
    def get(self, request):
    
        
        name = request.GET['name']
        time = request.GET['time']
        date = request.GET['date']
        room = request.GET['room']
        
        e = Event.objects.get_or_create(name=name,time=time,date=date,room=room)
        
        return HttpResponse(name)

# Fullcalendar test page
class FullcalendarTest(View):
    def get(self, request):
        context_dict = {}
        return render(request, 'booking_app/calendar_test.html', context=context_dict)
