"""acola_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from acola_web.views import paginas, usuarios

urlpatterns = [
    path('', paginas.index, name='home'),
    path('login', paginas.login, name='login'),
    path('logout', paginas.logout, name='logout'),
    path('usuarios', usuarios.index, name='usuarios.index'),
    path('usuarios/editar/dados/<id>', usuarios.editar_dados, name='usuarios.editar_usuario'),
    path('usuarios/editar/senha/<id>', usuarios.editar_senha, name='usuarios.editar_senha'),
]
