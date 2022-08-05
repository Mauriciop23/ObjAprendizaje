from django import forms
from Objetivos.models import Area, Objeto

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        exclude = ('idobjeto',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        exclude = ('idarea',)
