# # from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# # from django.conf import settings
# from celery.schedules import crontab
# # from django.contrib.auth import get_user_model


# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desafioTCS.settings')
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafioTCS.settings")
# app = Celery("desafioTCS",
#             broker= 'redis://127.0.0.1:6379',
#             backend='redis://127.0.0.1:6379',
#             task_serializer="json",
#             result_serializer="json",
#             accept_content=['application/json'])

# # app = Celery('desafioTCS')
# # app = Celery()

# # app.config_from_object('django.conf:settings', namespace='CELERY')

# # Celery Beat Settings
# # app.conf.beat_schedule = {
# #     'change-status-machine': {
# #         'task': 'gerenciamento.tasks.mudando_status_maquinas',
# #         'schedule': crontab(minute='*/1'),
# #         #'args': (2,)
# #     }
    
# # }

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(60.0, mudando_status_maquinas(sender), name='add every 60 seconds')


# # app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')



# @app.task
# def mudando_status_maquinas(self):
#     from gerenciamento.models import Maquina, Status, Evento
#     from login.models import User
#     users = get_user_model().objects.all()
#     # users = User.objects.all()
#     for user in users:
#         maquinas = Maquina.objects.filter(user_id=user.id).all()
#         status = Status.objects.filter(user_id=user.id).all()
#         # user = User.objects.filter(id=user.id).first()
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
#             print(f'Evento {user.username}')