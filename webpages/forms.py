from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 
            'password1', 'password2'
        )

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=150)
    password = forms.CharField(label="Password", max_length=150, widget=forms.PasswordInput)

    

