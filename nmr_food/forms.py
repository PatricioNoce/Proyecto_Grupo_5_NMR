from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User 

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class BuscarMenu(forms.Form):
  comida = forms.CharField(max_length=100)


class FormularioRegistroUsuario(UserCreationForm):
    name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=20, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    direccion = forms.CharField(max_length=20, label='Direccion', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'name', 'telefono', 'direccion', 'password1', 'password2')
  