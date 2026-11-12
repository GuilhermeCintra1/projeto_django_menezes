from django import forms
from .models import Cavalo


class CavaloForm(forms.ModelForm):
    class Meta:
        model = Cavalo
        fields = ['nome', 'idade', 'pai', 'mae', 'foto']
        labels = {'foto': 'Foto (opcional)'}
