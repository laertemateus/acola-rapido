'''
Páginas da aplicação
'''

from datetime import datetime
from traceback import print_exc
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import redirect, render

from acola_web.models import Usuario


class LoginForm(forms.Form):
    email = forms.CharField(label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput())


def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        try:
            print(form.cleaned_data)
            usuario = Usuario.objects.get(email=form.cleaned_data['email'],senha=form.cleaned_data['senha'])

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
            form.add_error(None, 'Usuário não encontrado')
    
    return render(request, 'login.html', {
        'form': form
    })

def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def index(request):
    return render(request, 'index.html',{

    })
