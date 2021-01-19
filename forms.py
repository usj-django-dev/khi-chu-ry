from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile


class CreateNewUser(UserCreationForm):
    username = forms.CharField(required=True, label="",
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password1 = forms.CharField(required=True,
                                label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    password2 = forms.CharField(required=True,
                                label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta():
        model = UserProfile
        exclude = ('user',)
