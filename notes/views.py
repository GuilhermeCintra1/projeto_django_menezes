from django.shortcuts import render, redirect
from .models import Cavalo, Cliente


def index(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'notes/index.html', {'clientes': clientes})


def novo_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        cliente.save()
        return redirect('index')
    else:
        return render(request, 'notes/novo_cliente.html')


def cavalos(request):
    cavalos = Cavalo.objects.all().order_by('nome')
    return render(request, 'notes/cavalos.html', {'cavalos': cavalos})


def cavalos_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cavalos = Cavalo.objects.filter(proprietario=cliente).order_by('nome')
    return render(request, 'notes/cavalos_cliente.html', {'cliente': cliente, 'cavalos': cavalos})


def novo_cavalo(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        pai = request.POST.get('pai')
        mae = request.POST.get('mae')
        cavalo = Cavalo(nome=nome, idade=idade, pai=pai, mae=mae, proprietario=cliente)
        cavalo.save()
        return redirect('cavalos_cliente', cliente_id=cliente.id)
    else:
        return render(request, 'notes/novo_cavalo.html', {'cliente': cliente})


def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')
        cliente.save()
        return redirect('index')
    else:
        return render(request, 'notes/editar_cliente.html', {'cliente': cliente})


def apagar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('index')


def editar_cavalo(request, cavalo_id):
    cavalo = Cavalo.objects.get(id=cavalo_id)
    if request.method == 'POST':
        cavalo.nome = request.POST.get('nome')
        cavalo.idade = request.POST.get('idade')
        cavalo.pai = request.POST.get('pai')
        cavalo.mae = request.POST.get('mae')
        cavalo.proprietario = Cliente.objects.get(id=request.POST.get('proprietario'))
        cavalo.save()
        return redirect('cavalos_cliente', cliente_id=cavalo.proprietario_id)
    else:
        clientes = Cliente.objects.all().order_by('nome')
        return render(request, 'notes/editar_cavalo.html', {'cavalo': cavalo, 'clientes': clientes})


def apagar_cavalo(request, cavalo_id):
    cavalo = Cavalo.objects.get(id=cavalo_id)
    cliente_id = cavalo.proprietario_id
    cavalo.delete()
    if cliente_id is not None:
        return redirect('cavalos_cliente', cliente_id=cliente_id)
    return redirect('cavalos')

