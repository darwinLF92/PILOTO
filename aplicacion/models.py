from django.contrib.auth.models import User, Group, Permission
from django.db import models

# Modelos para Usuarios, Roles y Permisos ya vienen incluidos en Django.
# User, Group y Permission están en django.contrib.auth.models.

# Modelo para Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para Proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo para Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo para Ventas
class Venta(models.Model):
    OPCIONES_PAGO = [
        ('contado', 'Contado'),
        ('credito', 'Crédito'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(max_length=10, choices=OPCIONES_PAGO)
    dias_credito = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"

# Modelo para Compras
class Compra(models.Model):
    OPCIONES_PAGO = [
        ('contado', 'Contado'),
        ('credito', 'Crédito'),
    ]
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pago = models.CharField(max_length=10, choices=OPCIONES_PAGO)
    dias_credito = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor}"

# Modelo para Cuentas por Cobrar
class CuentaCobrar(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    monto_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Cuenta por cobrar - {self.venta}"

# Modelo para Cuentas por Pagar
class CuentaPagar(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)
    monto_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Cuenta por pagar - {self.compra}"
