from django.db import models
# from django.db.models.fields import Datetime
from login.models import User
# from django.contrib.auth.models import User

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

class Evento(models.Model):
    data = models.DateTimeField(null=True)
    status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    maquina_id = models.ForeignKey(Maquina, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} + {self.data} + {self.status_id} + {self.maquina_id}"
