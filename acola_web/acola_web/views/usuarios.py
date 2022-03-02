'''
CRUD DOS USUÁRIOS EXISTENTES NO SISTEMA
'''

from django.core.paginator import Paginator
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from acola_web.utils import converter_senha
from acola_web.settings import PAGE_SIZE
from acola_web.models import Usuario


class UsuarioDadosForm(forms.ModelForm):
    '''
    Formulário para editar os dados do usuário
    '''
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'admin']



class UsuarioSenhaForm(forms.ModelForm):
    '''
    Formulário para editar os dados do usuário
    '''
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label='Confirmar senha')

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha != converter_senha(confirmar_senha):
            raise forms.ValidationError('Confirmação de senha incorreta')

        return cleaned_data

    def clean_senha(self):
        return converter_senha(self.cleaned_data['senha'])

    class Meta:
        model = Usuario
        fields = ['senha', 'confirmar_senha']
        widgets = {
            'senha': forms.PasswordInput()
        }


def index(request):
    '''
    Lista todos os usuários registrados no sistema
    '''
    pag = Paginator(Usuario.objects.filter(ativo=1).order_by('nome'), PAGE_SIZE)

    return render(request, 'usuarios/index.html', {
        'pag': pag,
        'items': pag.page(request.GET.get('pg', 1)),
    })


def editar_dados(request, id):
    '''
    Edita os dados de um usuário
    '''
    form = UsuarioDadosForm(request.POST or None, instance=get_object_or_404(Usuario, pk=id))

    if form.is_valid():
        form.save()
        return redirect('usuarios.index')

    return render(request, 'form.html', {
        'form': form,
        'titulo' : 'Atualizar dados do usuário'
    })

def editar_senha(request,id):
    '''
    Edita a senha do usuário
    '''
    form = UsuarioSenhaForm(request.POST or None, instance=get_object_or_404(Usuario, pk=id))

    if form.is_valid():
        form.save()
        return redirect('usuarios.index')

    print(form.data.get('senha'))

    return render(request, 'form.html', {
        'form': form,
        'titulo' : 'Atualizar senha de '+form.instance.nome
    })

def desativar(request,id):
    '''
    Desativa a conta de um usuário
    '''
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.ativo = False
    usuario.save()

    return redirect('usuarios.index')
