from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Vantagem
from .utils import get_coin_transfer_context, process_coin_exchange, process_coin_transfer, register_user, create_empresa_vantagem

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login')
def my_coins(request):
    template = loader.get_template('minhas-moedas.html')
    updated = False

    if request.method == 'POST':
        process_coin_transfer(request.user, request.POST.copy())
        updated = True

    context = get_coin_transfer_context(request.user, updated)
    if context is None:
        return redirect('/')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def exchange_coins(request):
    template = loader.get_template('exchange-coins.html')

    if request.method == 'POST':
        template = loader.get_template('exchange-success.html')
        context = process_coin_exchange(request.user, request.POST.copy())
    else:
        context = get_coin_transfer_context(request.user, False)

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def empresa_create_vantagem(request):
    template = loader.get_template('empresa-create-vantagem.html')

    if request.method == 'POST' and request.user.empresa:
        context = create_empresa_vantagem(request.POST.copy(), request.user.empresa)
    else:
        context = {
            'none': None
        }

    return HttpResponse(template.render(context, request))


@login_required(login_url='/login')
def empresa_minhas_vantagens(request):
    template = loader.get_template('vantagem/list.html')

    if request.user.empresa:
        context = {
            'vantagens': Vantagem.objects.filter(empresa=request.user.empresa).order_by('nome')
        }
    else:
        return redirect('/')

    return HttpResponse(template.render(context, request))


def cadastro(request, registration_type):
    template = loader.get_template('cadastro.html')

    if registration_type != 'aluno' and registration_type != 'empresa':
        return redirect('/')

    if request.method == 'POST':
        context = register_user(request.POST.copy(), registration_type)
    else:
        context = {'is_aluno': registration_type == 'aluno'}

    return HttpResponse(template.render(context, request))
