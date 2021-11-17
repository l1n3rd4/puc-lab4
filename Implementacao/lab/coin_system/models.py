from django.db import models

# Create your models here.
class Alunos:
    nome = ''
    email = ''
    CPF = ''
    RG = ''
    endereco = ''
    instituicaoEnsino = ''
    curso = ''

    def get_extrato_conta():
        pass

class Professores:
    nome = ''
    CPF = ''
    departamento = ''
    instituicaoEnsino = ''

    def get_extrato_conta():
        pass
    
class EmpresasParceiras:
    pass

class Moedas:
    moedas_professores_semestre = 1000
    

# Conta, Saldo, 