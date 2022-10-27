from django import forms
from NMR_Food.models import Cliente, menu

class ClienteForm(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['nombre','telefono', 'mail', 'direccion']

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class BuscarMenu(forms.Form):
  comida = forms.CharField(max_length=100)
  
class MenuForm(forms.ModelForm):
  class Meta:
    model = menu
    fields = ['comida','precio']