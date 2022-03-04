'''
Modelo das entidades do sistema
'''

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


def usuario_admin(user):
    '''
    Verifica se o usuário é do tipo Admin
    '''
    return user.admin

class Usuario(AbstractBaseUser):
    '''
    Entidade Usuário
    '''
    senha = models.CharField(max_length=100, verbose_name='Senha')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    email = models.CharField(max_length=200, verbose_name='E-mail',unique=True)
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    admin = models.BooleanField(default=False,verbose_name='Adminsitrador')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    ultimo_login = models.DateTimeField(verbose_name='Último acesso',null=True)
    USERNAME_FIELD = 'email'


    @property
    def password(self):
        return self.senha

    @property
    def last_login(self):
        return self.ultimo_login