from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Status, Maquina, Evento
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from django.contrib.auth.models import User
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from login.models import User
import json

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
        period = request.POST.get('period', False)

        if period:
            set_event_period(request, period)

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
        messages.add_message(request, messages.SUCCESS, f'M??quina criada com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'N??o foi poss??vel adicionar a M??quina')

def delete_maquina(class_id, request):
    try:
        maquina = Maquina.objects.filter(id=class_id).first()
        maquina.delete()
        messages.add_message(request, messages.SUCCESS, f'M??quina deletada com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'N??o foi poss??vel deletar a M??quina')
    
def atualiza_maquina(nome, class_id, request):
    try:
        maquina = Maquina.objects.filter(id=class_id).first()
        maquina.nome = nome
        maquina.save()
        messages.add_message(request, messages.SUCCESS, f'M??quina atualizada com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'N??o foi poss??vel atualizar a M??quina')

def criar_status(codigo, nome, user, request):
    try:
        status = Status()
        if codigo_exists(codigo):
            messages.add_message(request, messages.INFO, f'Este c??digo j?? existe')
        else:
            status.codigo = codigo
            status.nome = nome
            status.user_id = user
            status.save()
            messages.add_message(request, messages.SUCCESS, f'Status criado com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'N??o foi poss??vel adicionar o status')

def atualiza_status(codigo, nome, status_id, request):
    try:
        status = Status.objects.filter(id=status_id).first()

        if nome:
            status.nome = nome
            messages.add_message(request, messages.SUCCESS, f'Nome do status atualizado com sucesso')
            status.save()
        
        if codigo and codigo_exists(codigo):
            messages.add_message(request, messages.WARNING, f'C??digo j?? existente')
        elif codigo:
            status.codigo = codigo
            status.save()
            messages.add_message(request, messages.SUCCESS, f'C??digo atualizado com sucesso')
    except:
        messages.add_message(request, messages.WARNING, f'N??o foi poss??vel alterar o status')

def delete_status(status_id, request):
    try:
        status = Status.objects.filter(id=status_id)

        status.delete()
        messages.add_message(request, messages.SUCCESS, f'Status deletado com sucesso')
    except:
        messages.add_message(request, messages.SUCCESS, f'N??o foi poss??vel deletar o status')

def codigo_exists(codigo):
    return Status.objects.filter(codigo=codigo).exists()

def set_event_period(request, period):
    user = User.objects.filter(id=request.user.id).first()
    schedule, created = IntervalSchedule.objects.get_or_create(
    every=period,
    period=IntervalSchedule.MINUTES)

    try:
        PeriodicTask.objects.filter(id=user.periodic_task_id.id).first().delete()
    except:
        pass
    finally:
        pd = PeriodicTask.objects.create(interval=schedule,
            name=f'{request.user.username} change machine status',
            task='gerenciamento.tasks.mudando_status_maquinas',
            # args=json.dumps(['one', 'two']),
            args=json.dumps([user.id],)
            # kwargs=json.dumps()
        )

        pd.save()
        user.periodic_task_id = pd
        user.save()