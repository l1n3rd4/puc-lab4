from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    cpf = models.CharField(max_length=16)
    rg = models.CharField(max_length=24)
    endereco = models.CharField(max_length=240)
    instituicao_ensino = models.CharField(max_length=80)
    curso = models.CharField(max_length=80)
    saldo = models.IntegerField(default=0)


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=16)
    departamento = models.CharField(max_length=80)
    instituicao_ensino = models.CharField(max_length=80)
    saldo = models.IntegerField(default=0)


class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class Vantagem(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    foto = models.CharField(max_length=360, default='', blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)


class Transacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True, default=None)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    vantagem = models.ForeignKey(Vantagem, on_delete=models.CASCADE, null=True, blank=True, default=None)
    valor = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
