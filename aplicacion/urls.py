from django.urls import path
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectVie
from .views import (
    ClienteListView, ClienteDetailView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    # Similarmente, importa las vistas para Proveedor, Venta, etc. aquí
    reporte_ventas_vendedor,  # Ejemplo de ruta adicional
)

urlpatterns = [
    # Rutas para Clientes
    path('', RedirectView.as_view(url='/login/'), name='root-redirect-to-login'),
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/crear/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete'),
    
    # Rutas para Proveedores (ejemplo)
    # path('proveedores/', ProveedorListView.as_view(), name='proveedor-list'),
    # ... (Repite el patrón similar al de Cliente)
    
    # Rutas para Ventas, Compras, CuentaCobrar, CuentaPagar, etc.
    # (Puedes seguir un patrón similar al de Cliente y Proveedor para definir estas rutas)

    # Rutas adicionales
    path('reporte/ventas/vendedor/<int:vendedor_id>/', reporte_ventas_vendedor, name='reporte-ventas-vendedor'),
    # Agrega otras rutas de reportes y funcionalidades específicas aquí
]

