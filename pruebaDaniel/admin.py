from django.contrib import admin

# Register your models here.


from .models import Clientes, Productos, Facturas

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Facturas)
