from typing import Pattern
from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.indexCliente, name='indexCliente'),
    path('createCliente/', views.createCliente, name='createCliente'),
    path('editCliente/<int:id>/', views.editCliente, name='editCliente'),
    path('deleteCliente/<int:id>/', views.deleteCliente, name="deleteCliente"),
    path('indexProducto/', views.indexProducto, name="indexProducto"),
    path('createProducto/', views.createProducto, name='createProducto'),
    path('editProducto/<int:id>/', views.editProducto, name='editProducto'),
    path('deleteProducto/<int:id>/', views.deleteProducto, name="deleteProducto"),
]


