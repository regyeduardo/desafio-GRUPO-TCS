from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Status, Maquina, Evento

@login_required(login_url='/login')
def dashboard(request):

    return render(request, 'gerenciamento/dashboard.html', {})

def criar_status(codigo, nome):
    status = Status()

    status.codigo = 'codigo'
    status.nome = 'nome'

    # Checar se status existe
    # status.save()