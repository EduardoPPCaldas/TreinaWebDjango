from django.db import models

# Create your models here.
class Diarista(models.Model):
  nome_completo = models.CharField(
    max_length=100,
  )

  cpf = models.CharField(
    max_length=11,
    unique=True
  )

  email = models.EmailField(
    max_length=100,
    unique=True
  )

  telefone = models.CharField(
    max_length=11
  )

  logradouro = models.CharField(
    max_length=60
  )

  numero = models.IntegerField()

  bairro = models.CharField(
    max_length=30
  )

  complemento = models.CharField(
    max_length=100,
    blank=True
  )

  cep = models.CharField(
    max_length=8
  )

  cidade = models.CharField(max_length=120, null=False, blank=True)

  estado = models.CharField(max_length=2)

  codigo_ibge = models.IntegerField()

  foto_usuario = models.ImageField()