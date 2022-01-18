from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Status, Maquina, Evento
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.contrib.auth.models import User
from login.models import User


@csrf_exempt
@login_required(login_url='/login')
def dashboard(request):
    user = User.objects.filter(id = request.user.id).first()
    if request.method == 'POST':
        codigo = request.POST.get('codigo', False)
        nome = request.POST.get('nome', False)
        method = request.POST.get('_method', False)
        model_class = request.POST.get('_model_class', False)
        class_id = request.POST.get('_id', False)

        if model_class == 'status':
            if method == 'PUT':
                atualiza_status(codigo, nome, class_id, request)
            elif method == 'DELETE':
                delete_status(class_id, request)
            else:
                criar_status(codigo, nome, user, request)
        elif model_class == 'maquina':
            if method == 'PUT':
                atualiza_maquina(nome, class_id, request)
            elif method == 'DELETE':
                delete_maquina(class_id, request)
            else:
                criar_maquina(nome, user, request)

    user_id = request.user.id
    all_status = Status.objects.filter(user_id=user_id).all()
    maquinas = Maquina.objects.filter(user_id=user_id).all()
    eventos = Evento.objects.filter(user_id=user_id).all().order_by('-data')[:10]

    return render(request, 'gerenciamento/dashboard.html', {'all_status': all_status, 'maquinas': maquinas, 'eventos': eventos})



    

def criar_maquina(nome, user, request):
    try:
        Maquina.objects.create(nome=nome, user_id=user)
        messages.add_message(request, messages.SUCCESS, f'Máquina criada com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'Não foi possível adicionar a Máquina')

def delete_maquina(class_id, request):
    try:
        maquina = Maquina.objects.filter(id=class_id).first()
        maquina.delete()
        messages.add_message(request, messages.SUCCESS, f'Máquina deletada com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'Não foi possível deletar a Máquina')
    
def atualiza_maquina(nome, class_id, request):
    try:
        maquina = Maquina.objects.filter(id=class_id).first()
        maquina.nome = nome
        maquina.save()
        messages.add_message(request, messages.SUCCESS, f'Máquina atualizada com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'Não foi possível atualizar a Máquina')



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

def atualiza_status(codigo, nome, status_id, request):
    try:
        status = Status.objects.filter(id=status_id).first()

        if nome:
            status.nome = nome
            messages.add_message(request, messages.SUCCESS, f'Nome do status atualizado com sucesso')
            status.save()
        
        if codigo and codigo_exists(codigo):
            messages.add_message(request, messages.WARNING, f'Código já existente')
        elif codigo:
            status.codigo = codigo
            status.save()
            messages.add_message(request, messages.SUCCESS, f'Código atualizado com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'Não foi possível alterar o status')

def delete_status(status_id, request):
    try:
        status = Status.objects.filter(id=status_id)

        status.delete()
        messages.add_message(request, messages.SUCCESS, f'Status deletado com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'Não foi possível deletar o status')


def codigo_exists(codigo):
    return Status.objects.filter(codigo=codigo).exists()

# def print_message(request):
#     messages.add_message(request, messages.INFO, 'Este código já existe')

#     from django.http import HttpResponse
#     return HttpResponse('Sera que pode dar certo?')
