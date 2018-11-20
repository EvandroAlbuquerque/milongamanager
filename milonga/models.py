from django.db import models


class Milonga(models.Model):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return str(self.data)


class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome


class Danca(models.Model):
    milonga = models.ForeignKey(Milonga, on_delete=models.PROTECT)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    cavalheiro = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='cavalheiro')
    dama = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='dama')

    def __str__(self):
        return f'{self.hora_inicio} - {self.hora_fim}'

    class Meta:
        verbose_name = "Dança"
        verbose_name_plural = "Danças"


# class Salao(models.Model):
#     capacidade_total = models.IntegerField()
#     capacidade_dancando = models.IntegerField()