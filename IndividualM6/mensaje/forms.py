from django import forms 
from .models import Formulario1, Publicacion

class NuevoForm(forms.ModelForm):
    cuerpo = forms.CharField(required = True)

    class Meta:
        model = Formulario1
        fields = ["cuerpo"]