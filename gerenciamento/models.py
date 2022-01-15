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
    codigo_status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    data = models.DateTimeField(null=True)
    codigo_status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id} + {self.data} + {self.codigo_status}"