from django.shortcuts import render, redirect
from .models import Cavalo, Cliente


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        cliente.save()
        return redirect('index')
    else:
        all_clientes = Cliente.objects.all().order_by('nome')
        return render(request, 'notes/index.html', {'clientes': all_clientes})


def cavalos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        pai = request.POST.get('pai')
        mae = request.POST.get('mae')
        proprietario = request.POST.get('proprietario')

        cavalo = Cavalo(nome=nome, idade=idade, pai=pai, mae=mae, proprietario=proprietario)
        cavalo.save()
        return redirect('cavalos')
    else:
        all_cavalos = Cavalo.objects.all().order_by('nome')
        return render(request, 'notes/cavalos.html', {'cavalos': all_cavalos})
