# # from django.contrib.auth import get_user_model

# from celery import shared_task
# from datetime import datetime
# from django.utils import timezone
# from .models import Maquina, Status, Evento
# from login.models import User
# from celery.decorators import periodic_task
# from datetime import timedelta



# @periodic_task(run_every=timedelta(minutes=1))
# def mudando_status_maquinas(self):
#     # users = get_user_model().objects.all()
#     users = User.objects.all()
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
    