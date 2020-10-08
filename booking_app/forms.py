from django import forms
from django.contrib.auth.models import User
from booking_app.models import UserProfile

# Two classes inheriting from forms.ModelForm.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

"""
booking_app form.py
"""
