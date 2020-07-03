from django import forms
from .models import *

class registerForm(forms.ModelForm):

    class Meta:
        model = teacherRegister
        fields = '__all__'

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your username'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Your Password'}
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Your Password'}
        )
    )

class teacherLoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your username'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        )
    )