from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cavalos/', views.cavalos, name='cavalos'),
]
