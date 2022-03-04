
'''
Páginas relacionadas à manipulação dos susuários do sistema
'''

from django.shortcuts import render
from acola_web.models import Usuario, usuario_admin
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(usuario_admin)
def index(request):
    '''
    Lista todos os usuários ativos
    '''
    return render(request,'usuarios/index.html',{
        'usuarios' : Usuario.objects.filter(ativo=True).all()
    })