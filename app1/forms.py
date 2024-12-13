from django import forms
from .models import Cliente

class CreateUser(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'endereco']

        

