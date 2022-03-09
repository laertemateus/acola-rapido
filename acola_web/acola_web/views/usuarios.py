
'''
Páginas relacionadas à manipulação dos susuários do sistema
'''

from email import message
from django.contrib import messages
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from acola_web.models import Usuario, usuario_admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password

class UsuarioDadosForm(forms.ModelForm):
    '''
    Formulário para editar os dados do usuário
    '''
    class Meta:
        model = Usuario
        fields = ['nome','email','admin']


class UsuarioSenhaForm(forms.ModelForm):
    '''
    Formulário para editar a senha do usuário
    '''

    senha = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirma_senha = forms.CharField(max_length=200,label='Confirmar senha', widget=forms.PasswordInput())
    
    class Meta:
        model = Usuario
        fields = ['senha']

    def clean_senha(self):
        print(">", self.data.get('senha'), self.data.get('confirma_senha'))
        if self.data.get('senha') != self.cleaned_data.get('confirma_senha'):
            raise forms.ValidationError('Confirmação de senha inválida')

        return make_password(self.data.get('senha'))

@user_passes_test(usuario_admin)
def index(request):
    '''
    Lista todos os usuários ativos
    '''
    return render(request,'usuarios/index.html',{
        'usuarios' : Usuario.objects.filter(ativo=True).all()
    })

@user_passes_test(usuario_admin)
def editar_dados(request, id):
    '''
    Edita os dados de um usuário
    '''
    form = UsuarioDadosForm(request.POST or None, instance=Usuario.objects.get(pk=id))

    if form.is_valid():
        form.save()
        messages.success(request,'Usuário %s atualizado com sucesso'%(form.cleaned_data['nome']))
        return redirect('usuarios.index')

    return render(request, 'form.html', {
        'form': form,
        'titulo': 'Editar dados do usuário',
        'url_voltar': 'usuarios.index'
    })


@user_passes_test(usuario_admin)
def editar_senha(request,id):
    '''
    Edita a senha do usuário
    '''
    form = UsuarioSenhaForm(request.POST or None, instance=Usuario.objects.get(pk=id))

    if form.is_valid():
        form.save()
        messages.success(request,'Senha do usuário %s atualizada com sucesso'%form.instance.nome)
        return redirect('usuarios.index')

    return render(request, 'form.html',{
        'form':form,
        'titulo':'Alterar senha do usuário',
        'url_voltar':'usuarios.index'
    })

@user_passes_test(usuario_admin)
def excluir(request,id):
    usuario = get_object_or_404(Usuario, id)
    usuario.ativo=False
    usuario.save()
    messages.success('Usuário excluído com sucesso')
    return redirect('usuarios.index')
