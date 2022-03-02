from datetime import datetime
from tkinter import Widget
from django.db import models
from django.forms import PasswordInput
from acola_web.settings import SECRET_KEY

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    senha = models.CharField(max_length=32)
    nascimento = models.DateField()
    admin = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    ativo = models.BooleanField(default=True)