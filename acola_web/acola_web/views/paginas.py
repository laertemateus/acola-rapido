'''
Páginas da aplicação
'''

from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
from traceback import print_exc
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import redirect, render

from acola_web.models import Usuario


class LoginForm(forms.Form):
    '''
    Fomrulário para login
    '''
    email = forms.CharField(label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput())


def login(request):
    form = LoginForm(request.POST or None)

    # Redireciona a página caso já exista um usuário autenticado    
    if request.user.is_authenticated:
        return redirect('/')

    # Formulário foi preenchido
    if form.is_valid():
        try:
            # Busca o usuário
            usuario = Usuario.objects.get(email=form.cleaned_data['email'])

            if not check_password(form.cleaned_data['senha'], usuario.senha):
                raise Exception()
            
            if usuario.ativo:
                auth.login(request, usuario)

                # Atualiza o último login
                usuario.ultimo_login = datetime.now()
                usuario.save()

                # redireciona para a página desejada
                return redirect(request.GET.get('next'))
            else:
                form.add_error(None, 'Usuário não está ativo no sistema')
        except:
            form.add_error(None, 'Usuário ou senha inválidos')
    
    return render(request, 'login.html', {
        'form': form
    })

def logout(request):
    '''
    Ação de Logout
    '''
    auth.logout(request)
    return redirect('home')


def index(request):
    return render(request, 'index.html',{

    })
