from django.contrib import admin
from .models import Restaurante, Hotel, Zona_Turistica, Hotel_Proveedor, Restaurante_Proveedor

# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Hotel)
admin.site.register(Zona_Turistica)
admin.site.register(Hotel_Proveedor)
admin.site.register(Restaurante_Proveedor)
