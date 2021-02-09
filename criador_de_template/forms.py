from django import forms
from .models import Planilha


class PlanilhaForm(forms.ModelForm):
    class Meta:
        model = Planilha
        fields = ('cliente', 'documento')
            
        labels = {
        'cliente': False,
        'documento': False,
            }
        
        widgets = {
            'cliente': forms.TextInput(attrs={'placeholder': 'Nome do Cliente'}),
            }
