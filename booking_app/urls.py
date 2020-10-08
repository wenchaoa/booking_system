from django.urls import path
from booking_app import views

app_name = 'booking_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('building/<slug:building_name_slug>/',views.ShowBuildingView.as_view(), name='show_building'),
    path('building/<slug:building_name_slug>/<slug:room_name_slug>/',views.ShowRoomView.as_view(), name='show_room'),
    path('registration/', views.register, name='register'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    
    # Ajax Test
    path('test/', views.Test.as_view(), name='test'),
    path('like_building/', views.LikeBuildingView.as_view(), name='like_building'),
    
    # Fullcalendar test
    path('fullcalendar_test/', views.FullcalendarTest.as_view(), name='fullcalendar_test'),
]
