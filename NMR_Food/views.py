from django.shortcuts import render
from NMR_Food.models import Cliente
from django.views import View
from NMR_Food.forms import ClienteForm, Buscar
# Create your views here.

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
    