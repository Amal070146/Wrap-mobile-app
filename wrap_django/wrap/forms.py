from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'photo']
        fields = ['name', 'email']