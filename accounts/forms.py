from django import forms
from django.contrib.auth.models import User

from .models import Rockleton

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User  
        fields = ('username', 'email', 'password')

class RockletonForm(forms.ModelForm):
    class Meta:
        model = Rockleton
        exclude = ['user']

        
