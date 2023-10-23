from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Proveedor, Venta, Compra, CuentaCobrar, CuentaPagar
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'login.html'

# Vistas para Clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente_list.html"

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'direccion']
    template_name = "cliente_form.html"
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono', 'direccion']
    template_name = "cliente_form.html"
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente_confirm_delete.html"
    success_url = reverse_lazy('cliente-list')

# Puedes repetir este patrón para Proveedor, Venta, Compra, CuentaCobrar, CuentaPagar.

# Vistas adicionales (como ejemplo)
from django.shortcuts import render

def reporte_ventas_vendedor(request, vendedor_id):
    ventas = Venta.objects.filter(vendedor__id=vendedor_id)
    # Aquí puedes agregar lógica adicional para el reporte.
    return render(request, "reporte_ventas_vendedor.html", {'ventas': ventas})

# Y así sucesivamente para otros reportes y funcionalidades específicas.


