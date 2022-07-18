from django import forms
from Objetivos.models import objeto

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = objeto
        exclude = ('idobjeto',)
