from celery import shared_task
# from celery import Task
from desafioTCS.celery import app
from .models import Status, Maquina, Evento
import json
import random
from datetime import datetime
from login.models import User
from celery.contrib import rdb

@app.task(bind=True)
def mudando_status_maquinas(self, *args, **kwargs):
    current_user = User.objects.filter(id=args[0]).first()
    maquinas = Maquina.objects.filter(user_id=current_user).all()
    status = Status.objects.filter(user_id=current_user).all()
    for maquina in maquinas:
        selected_status = random.choice(status)
        maquina.status_id = selected_status
        maquina.save()

        evento = Evento()
        evento.status_id = selected_status
        evento.maquina_id = maquina
        evento.user_id = current_user
        evento.data = datetime.now()
        evento.save()
        print(f'Evento {current_user.username}')