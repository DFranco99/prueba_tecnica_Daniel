
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Clientes, Productos, Facturas
from .forms import clienteForm, productoForm

# Create your views here.



def indexCliente(request):
    clientes = Clientes.objects.all()
    context = {'clientes': clientes} 
    return render(request, 'pruebaDaniel/indexCliente.html', context)

def createCliente(request):
    if request.method == 'GET':
        form = clienteForm()
        context = {
            'form': form
        }
    else:
        form = clienteForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect(indexCliente)
    return render(request, 'pruebaDaniel/createCliente.html', context)



def editCliente(request, id):
    cliente = Clientes.objects.get(id = id)
    if request.method == 'GET':
        form= clienteForm(instance=cliente)
        context= {
            'form': form
        } 
    else:
        form= clienteForm(request.POST, instance=cliente)
        context= {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('indexCliente')

    return render(request, 'PruebaDaniel/createCliente.html', context)


def deleteCliente(request,id):
    cliente= Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('indexCliente') 

#=====================================================


def indexProducto(request):
    productos = Productos.objects.all()
    context = {'productos': productos} 
    return render(request, 'pruebaDaniel/indexProducto.html', context)

def createProducto(request):
    if request.method == 'GET':
        form = productoForm()
        context = {
            'form': form
        }
    else:
        form = productoForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect(indexProducto)
    return render(request, 'pruebaDaniel/createProducto.html', context)

def editProducto(request, id):
    producto = Productos.objects.get(id = id)
    if request.method == 'GET':
        form= productoForm(instance=producto)
        context= {
            'form': form
        } 
    else:
        form= productoForm(request.POST, instance=producto)
        context= {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('indexProducto')

    return render(request, 'pruebaDaniel/createProducto.html', context)

def deleteProducto(request,id):
    producto= Productos.objects.get(id=id)
    producto.delete()
    return redirect('indexProducto') 