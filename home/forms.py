from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class MeuAutoForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password' ]
    
    def __init__(self, *args, **kwargs):
        super(MeuAutoForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'})
        self.fields['password'].label = False
