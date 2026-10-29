from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'telefone', 'email')
        widgets = {'telefone': forms.TextInput(attrs={'type': 'tel'})}
