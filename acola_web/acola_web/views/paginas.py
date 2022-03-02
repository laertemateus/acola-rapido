from django.shortcuts import redirect, render
from django import forms
from acola_web.models import Usuario
from acola_web.utils import converter_senha

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,label='E-mail')
    senha = forms.CharField(widget=forms.PasswordInput, required=True)


def home(request):
    '''
    Página incial do site
    '''

    return render(request, 'paginas/home.html', {})


def login(request):
    '''
    Página de login
    '''
    loginForm = LoginForm(request.POST)

    # Usuário já está logado, não precisa fazer login
    if 'usuario_id' in request.session:
        return redirect('home')

    # Formulário válido, testa se pode ser feito o login
    if loginForm.is_valid():
        usuario = Usuario.objects.get(email=loginForm.cleaned_data['email'], senha=converter_senha(loginForm.cleaned_data['senha']))

        # Se o usuário não for encontrado mostrar erro
        # Senão registrar usuário na session e redirecionar
        if usuario is None:
            loginForm.add_error(None, 'Usuário ou senha inválidos')
        else:
            request.session['usuario_id'] = usuario.id
            request.session['usuario_nome'] = usuario.nome
            request.session['usuario_adm'] = usuario.admin
            return redirect('home')

    return render(request, 'paginas/login.html', {
        'form': loginForm
    })

def logout(request):
    '''
    Ação de deslogar o usuário do sistema
    '''
    del request.session['usuario_id']
    
    return redirect('home')