from django.shortcuts import render
from NMR_Food.models import Cliente, Configuracion, menu, Informacion
from django.views import View
from NMR_Food.forms import ClienteForm, Buscar, MenuForm, BuscarMenu

# Create your views here.
def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'NMR_Food/index.html', {'configuracion': configuracion})

class AltaCliente(View):

    form_class = ClienteForm
    template_name = 'NMR_Food/alta_cliente.html'
    initial = {"nombre":"", "telefono":"", "mail":"", "direccion":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el cliente {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

def mostrar_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "NMR_Food/clientes.html", {"lista_clientes": lista_clientes})


class BuscarCliente(View):

    form_class = Buscar
    template_name = 'NMR_Food/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_clientes = Cliente.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_clientes':lista_clientes})

        return render(request, self.template_name, {"form": form})
    
    
def mostrar_menu(request):
    lista_menu = menu.objects.all()
    return render(request, "NMR_Food/lista_menu.html", {"lista_menu": lista_menu})

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
            lista_menu = menu.objects.filter(comida__icontains=comida).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_menu':lista_menu})

        return render(request, self.template_name, {"form": form})

class armar_menu():
    pass

def about(request):
    informacion = Informacion.objects.first()
    return render(request, 'NMR_Food/about.html', {'informacion': informacion})