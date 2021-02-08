from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Cadastro(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text=False)
    last_name = forms.CharField(max_length=100, help_text=False)
    email = forms.EmailField(max_length=150)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(Cadastro, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
