from django.db import models


# Create your models here.
class Restaurante(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre del Restaurante')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return"{0} {1} :: {2}".format(self.name, self.address, self.phone)

class Meta:
    verbose_name='Restaurante'
    verbose_name_plural='Restaurantes'


class Hotel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre del Hotel')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return"{0} {1} :: {2}".format(self.name, self.address, self.phone)

class Meta:
    verbose_name='Hotel'
    verbose_name_plural='Hoteles'

class Zona_Turistica(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre de la Zona Turistica')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')

    def __str__(self):
        return"{0} {1} :: {2}".format(self.name, self.address, self.phone)

class Meta:
    verbose_name='Zona Turisticas'
    verbose_name_plural='Zonas Turisticas'
            
class Hotel_Proveedor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Empresa')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    email = models.EmailField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return self.name

class Meta:
    verbose_name= 'Proveedor de Hotele'
    verbose_name_plural='Proveerdores de Hoteles'


class Restaurante_Proveedor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Empresa')    
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    email = models.EmailField(max_length=50, verbose_name='E-mail')

    def __str__(self):
        return self.name 

class Meta:
    verbose_name= 'Proveedor de Restaurante'
    verbose_name_plural='Proveedor de Restaurantes'

    def __str__(self):
        return self.name

