from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('proprietarios/', views.index, name='index'),
    path('proprietarios/novo/', views.novo_cliente, name='novo_cliente'),
    path('proprietarios/<int:cliente_id>/cavalos/', views.cavalos_cliente, name='cavalos_cliente'),
    path('proprietarios/<int:cliente_id>/cavalos/novo/', views.novo_cavalo, name='novo_cavalo'),
    path('clientes/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:cliente_id>/apagar/', views.apagar_cliente, name='apagar_cliente'),
    path('cavalos/', views.cavalos, name='cavalos'),
    path('cavalos/<int:cavalo_id>/', views.editar_cavalo, name='editar_cavalo'),
    path('cavalos/<int:cavalo_id>/apagar/', views.apagar_cavalo, name='apagar_cavalo'),
]

