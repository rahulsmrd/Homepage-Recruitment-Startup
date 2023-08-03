from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from home.models import *

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model=get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'

class profile_form(forms.ModelForm):
    class Meta():
        model=profile
        fields=()

class post_form(forms.ModelForm):
    class Meta():
        model=posts
        fields='__all__'