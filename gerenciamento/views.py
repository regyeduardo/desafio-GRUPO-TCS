from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Status, Maquina, Evento
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User

@csrf_exempt
@login_required(login_url='/login')
def dashboard(request):
    user = User.objects.filter(id = request.user.id).first()
    if request.method == 'POST':
        codigo = request.POST.get('codigo', False)
        nome = request.POST.get('nome', False)
        method = request.POST.get('_method', False)

        if method == 'PUT':
            pass
        elif method == 'DELETE':
            pass
        else:
            criar_status(codigo, nome, user, request)

    user_id = request.user.id
    all_status = Status.objects.filter(user_id=user_id).all()

    return render(request, 'gerenciamento/dashboard.html', {'all_status': all_status})

def criar_status(codigo, nome, user, request):
    try:
        status = Status()
        if codigo_exists(codigo):
            messages.add_message(request, messages.INFO, f'Este código já existe')
        else:
            status.codigo = codigo
            status.nome = nome
            status.user_id = user
            status.save()
            messages.add_message(request, messages.SUCCESS, f'Status criado com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'Não foi possível adicionar o status')

def atualiza_status(codigo, nome, status_id):
    try:
        status = Status.objects.filter(id=status_id).first()

        if nome:
            status.nome = nome
        
        if codigo:
            status.codigo = codigo
        
        status.save()
        return True
    except:
        return False



def codigo_exists(codigo):
    return Status.objects.filter(codigo=codigo).exists()

# def print_message(request):
#     messages.add_message(request, messages.INFO, 'Este código já existe')

#     from django.http import HttpResponse
#     return HttpResponse('Sera que pode dar certo?')
