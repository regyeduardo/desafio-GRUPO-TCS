from django.apps import AppConfig
# import random
# from datetime import datetime
# from .models import Status, Maquina, Evento


class GerenciamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gerenciamento'

    # def ready(self):
    #     import schedule
    #     import time
        # from celery import Celery
        # from celery.schedules import crontab
        # crontab(minute='*/15')
    #     self.get_model('Status')
        # maquinas = Maquina.objects.filter(user_id=request.user.id).all()
        # status = Status.objects.filter(user_id=request.user.id).all()
        # user = User.objects.filter(id=request.user.id).first()
        # for maquina in maquinas:
        #     selected_status = random.choice(status)
        #     maquina.status_id = selected_status
        #     maquina.save()

        #     evento = Evento()
        #     evento.status_id = selected_status
        #     evento.maquina_id = maquina
        #     evento.user_id = user
        #     evento.data = datetime.now()
        #     evento.save()

# class EventChangeMaquina(AppConfig):
#     name = 'Setando Evento'
#     def ready(self):
#         maquinas = Maquina.objects.filter(user_id=request.user.id).all()
#         status = Status.objects.filter(user_id=request.user.id).all()
#         user = User.objects.filter(id=request.user.id).first()
#         for maquina in maquinas:
#             selected_status = random.choice(status)
#             maquina.status_id = selected_status
#             maquina.save()

#             evento = Evento()
#             evento.status_id = selected_status
#             evento.maquina_id = maquina
#             evento.user_id = user
#             evento.data = datetime.now()
#             evento.save()
    #     def set_event_machine_status(request):
    # maquinas = Maquina.objects.filter(user_id=request.user.id).all()
    # status = Status.objects.filter(user_id=request.user.id).all()
    # user = User.objects.filter(id=request.user.id).first()
    # for maquina in maquinas:
    #     selected_status = random.choice(status)
    #     maquina.status_id = selected_status
    #     maquina.save()

    #     evento = Evento()
    #     evento.status_id = selected_status
    #     evento.maquina_id = maquina
    #     evento.user_id = user
    #     evento.data = datetime.now()
    #     evento.save()