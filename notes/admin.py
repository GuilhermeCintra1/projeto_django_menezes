from django.contrib import admin
from .models import Cavalo, Cliente
from .forms import ClienteForm


admin.site.register(Cavalo)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
    list_display = ('nome', 'telefone', 'email')
    search_fields = ('nome', 'telefone', 'email')
