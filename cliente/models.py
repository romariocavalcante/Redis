from django.db import models


class herois(models.Model):

    nome = models.CharField('Nome', max_length=150)

    universo = models.CharField('Nome', max_length=150)

    habilidade = models.CharField('Nome', max_length=150)

    def __str__(self):
        return self.nome

