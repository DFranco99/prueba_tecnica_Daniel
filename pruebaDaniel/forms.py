from django import forms
from django.db.models import fields
from .models import Clientes, Productos


class clienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'


class productoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        