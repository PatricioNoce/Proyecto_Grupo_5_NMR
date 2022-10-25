from django import forms
from NMR_Food.models import Cliente

class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nombre','telefono', 'mail', 'direccion']

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)