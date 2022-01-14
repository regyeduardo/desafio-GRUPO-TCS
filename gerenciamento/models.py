from django.db import models

class Status(models.Model):
    codigo = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
        
class Maquina(models.Model):
    nome = models.CharField(max_length=30)
    codigo_status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    data = models.DateField()
    codigo_status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} + {self.data} + {self.codigo_status}"