from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Cadastro(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text=False)
    last_name = forms.CharField(max_length=100, help_text=False)
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)