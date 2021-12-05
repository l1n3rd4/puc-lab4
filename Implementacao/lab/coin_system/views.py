from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .utils import get_coin_transfer_context, process_coin_exchange, process_coin_transfer

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
    template = loader.get_template('exchange-success.html')

    if request.method == 'POST':
        context = process_coin_exchange(request.user, request.POST.copy())
    else:
        return redirect('/')

    return HttpResponse(template.render(context, request))
