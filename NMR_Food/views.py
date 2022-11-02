from tkinter import Menu
from django.shortcuts import render, redirect
from NMR_Food.models import Cliente, Configuracion, Menu, Informacion
from django.views import View
from NMR_Food.forms import ClienteForm, Buscar, BuscarMenu, FormularioRegistroUsuario
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login


def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'NMR_Food/index.html', {'configuracion': configuracion})
    
class BuscarMenu(View):

    form_class = BuscarMenu
    template_name = 'NMR_Food/buscar_menu.html'
    initial = {"comida":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            comida = form.cleaned_data.get("comida")
            lista_menu = Menu.objects.filter(comida__icontains=comida).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_menu':lista_menu})

        return render(request, self.template_name, {"form": form})

class armar_menu():
    pass

def about(request):
    informacion = Informacion.objects.first()
    return render(request, 'NMR_Food/about.html', {'informacion': informacion})



class ListMenu(ListView):
  model = Menu

class CreateMenu(CreateView):
  model = Menu
  success_url = "/panel-menu"
  fields = ["comida", "precio"]

class DetailMenu(DetailView):
    model=Menu

class DeleteMenu(DeleteView):
  model = Menu
  success_url = reverse_lazy("list-menu")

class UpdateMenu(UpdateView):
  model = Menu
  success_url = "/panel-menu"
  fields = ["comida", "precio"]

class SearchPostByName(ListView):
    def get_queryset(self):
        menu_comida = self.request.GET.get('menu-comida')
        return Post.objects.filter(comida__icontains=menu_comida)      


class Nmr_Login(LoginView):
    template_name = 'NMR_Food/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'NMR_Food/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class Nmr_Logout(LogoutView):
    template_name = 'NMR_Food/logout.html'    


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'NMR_Food/index.html'