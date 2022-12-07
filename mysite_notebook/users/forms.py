from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Prisijungimo vardas',
            'email': 'El.paštas',
            'password1': 'Slaptažodis',
            'password2': 'Pakartokite slaptažodį'
        }
        help_texts = {
            'password1': None,
            'password2': None,
        }
