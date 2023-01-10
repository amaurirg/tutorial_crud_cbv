from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
