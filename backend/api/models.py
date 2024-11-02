from django.db import models

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    clinica = models.ForeignKey(Clinica, related_name='medicos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"