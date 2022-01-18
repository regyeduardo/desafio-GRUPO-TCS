from django.db import models
# from django.db.models.fields import Datetime
from django.contrib.auth.models import User

class Status(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
class Maquina(models.Model):
    nome = models.CharField(max_length=20)
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

def set_event_machine_status(self):
        maquinas = Maquina.objects.filter(user_id=self.user_id).all()
        status = Status.objects.filter(user_id=self.user_id).all()
        # user = User.objects.filter(id=request.user.id).first()
        for maquina in maquinas:
            selected_status = random.choice(status)
            maquina.status_id = selected_status
            maquina.save()

            evento = Evento()
            evento.status_id = selected_status
            evento.maquina_id = maquina
            evento.user_id = self.user_id
            evento.data = datetime.now()
            evento.save()
            print("BALALALALLALA")

class Evento(models.Model):
    data = models.DateTimeField(null=True)
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    maquina_id = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    periodo = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} + {self.data} + {self.status_id} + {self.maquina_id}"
    
    def update_status(self):
        import schedule
        import time

        if self.periodo:
            schedule.every(self.periodo).minutes.do(set_event_machine_status(self))

