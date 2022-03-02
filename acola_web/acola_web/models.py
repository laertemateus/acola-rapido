from django.db import models
from acola_web.settings import SECRET_KEY

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    senha = models.CharField(max_length=32)
    nascimento = models.DateField()
    admin = models.BooleanField(default=False)