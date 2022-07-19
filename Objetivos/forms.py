from django import forms
from Objetivos.models import Objeto

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        exclude = ('idobjeto',)
