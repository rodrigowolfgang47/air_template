from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from criador_de_template.models import Usuario

class Cadastro(UserCreationForm):
    UF_CHOICES = (
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
    )

    first_name = forms.CharField(max_length=100, help_text=False)
    last_name = forms.CharField(max_length=100, help_text=False)
    email = forms.EmailField(max_length=150)
    celular = forms.CharField(max_length=11, min_length=11)
    estado = forms.ChoiceField(choices=UF_CHOICES)


    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
'email', 'password1', 'password2', 'celular', 'estado')

    def __init__(self, *args, **kwargs):
        super(Cadastro, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'})
        self.fields['celular'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular ex:11948719660'})
