from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Cavalo, Cliente
from .forms import CavaloForm


def criar_conta(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    form = UserCreationForm()
    erro = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        nome = request.POST.get('nome', '').strip()
        sobrenome = request.POST.get('sobrenome', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        email = request.POST.get('email', '').strip()

        if not nome or not sobrenome or not telefone or not email:
            erro = 'Preencha nome, sobrenome, telefone e email.'
        elif len(nome) > 150 or len(sobrenome) > 150 or len(nome + ' ' + sobrenome) > 200 or len(telefone) > 30 or len(email) > 254:
            erro = 'Nome, sobrenome, telefone ou email ultrapassou o tamanho permitido.'
        elif form.is_valid():
            with transaction.atomic():
                usuario = form.save(commit=False)
                usuario.first_name = nome
                usuario.last_name = sobrenome
                usuario.email = email
                usuario.save()
                cliente = Cliente(usuario=usuario, nome=nome + ' ' + sobrenome, telefone=telefone, email=email)
                cliente.save()
            return redirect('login')

    return render(request, 'registration/criar_conta.html', {
        'form': form,
        'erro': erro,
        'dados': request.POST,
    })


@login_required
def index(request):
    if not request.user.is_staff:
        return redirect('cavalos')
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'notes/index.html', {'clientes': clientes})


@login_required
def novo_cliente(request):
    if not request.user.is_staff:
        return redirect('index')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        cliente.save()
        return redirect('index')
    else:
        return render(request, 'notes/novo_cliente.html')


@login_required
def cavalos(request):
    if request.user.is_staff:
        cavalos = Cavalo.objects.all().order_by('nome')
        clientes = Cliente.objects.all().order_by('nome')
    else:
        cavalos = Cavalo.objects.filter(proprietario__usuario=request.user).order_by('nome')
        clientes = Cliente.objects.filter(usuario=request.user)
    return render(request, 'notes/cavalos.html', {'cavalos': cavalos, 'clientes': clientes})


@login_required
def cavalos_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if not request.user.is_staff and cliente.usuario != request.user:
        return redirect('index')
    cavalos = Cavalo.objects.filter(proprietario=cliente).order_by('nome')
    return render(request, 'notes/cavalos_cliente.html', {'cliente': cliente, 'cavalos': cavalos})


@login_required
def novo_cavalo(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if not request.user.is_staff and cliente.usuario != request.user:
        return redirect('index')
    if request.method == 'POST':
        form = CavaloForm(request.POST, request.FILES)
        if form.is_valid():
            cavalo = form.save(commit=False)
            cavalo.proprietario = cliente
            cavalo.save()
            return redirect('cavalos_cliente', cliente_id=cliente.id)
    else:
        form = CavaloForm()
    return render(request, 'notes/novo_cavalo.html', {'cliente': cliente, 'form': form})


@login_required
def editar_cliente(request, cliente_id):
    if not request.user.is_staff:
        return redirect('index')
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')
        cliente.save()
        return redirect('index')
    else:
        return render(request, 'notes/editar_cliente.html', {'cliente': cliente})


@login_required
def apagar_cliente(request, cliente_id):
    if not request.user.is_staff:
        return redirect('index')
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('index')


@login_required
def editar_cavalo(request, cavalo_id):
    if not request.user.is_staff:
        if not Cavalo.objects.filter(id=cavalo_id, proprietario__usuario=request.user).exists():
            return redirect('cavalos')
    cavalo = Cavalo.objects.get(id=cavalo_id)
    if request.method == 'POST':
        form = CavaloForm(request.POST, request.FILES, instance=cavalo)
        if form.is_valid():
            cavalo = form.save(commit=False)
            if request.user.is_staff:
                cavalo.proprietario = Cliente.objects.get(id=request.POST.get('proprietario'))
            cavalo.save()
            return redirect('cavalos_cliente', cliente_id=cavalo.proprietario_id)
    else:
        form = CavaloForm(instance=cavalo)
    if request.user.is_staff:
        clientes = Cliente.objects.all().order_by('nome')
    else:
        clientes = Cliente.objects.filter(usuario=request.user)
    return render(request, 'notes/editar_cavalo.html', {'cavalo': cavalo, 'clientes': clientes, 'form': form})


@login_required
def apagar_cavalo(request, cavalo_id):
    if not request.user.is_staff:
        if not Cavalo.objects.filter(id=cavalo_id, proprietario__usuario=request.user).exists():
            return redirect('cavalos')
    cavalo = Cavalo.objects.get(id=cavalo_id)
    cliente_id = cavalo.proprietario_id
    cavalo.delete()
    if cliente_id is not None:
        return redirect('cavalos_cliente', cliente_id=cliente_id)
    return redirect('cavalos')

