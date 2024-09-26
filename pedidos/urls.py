from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_pedidos/', views.cadPedidos, name ='cadPedidos'),
    
]