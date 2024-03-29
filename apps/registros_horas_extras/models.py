from django.db import models

from apps.funcionarios.models import Funcionario


class HorasExtras(models.Model):
    motivo = models.CharField(max_length=10)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
