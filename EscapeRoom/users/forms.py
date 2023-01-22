from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    types = [('W','Wlasciciel'),
            ('K','Klient'),
            ]
    type = forms.ChoiceField(choices=types)
    class Meta:
        model = User
        fields = ['username','email','password1','password2','type',]