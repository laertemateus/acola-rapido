# Generated by Django 4.0.3 on 2022-03-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=100, verbose_name='Senha')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='E-mail')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('admin', models.BooleanField(default=False, verbose_name='Adminsitrador')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('ultimo_login', models.DateTimeField(verbose_name='Último acesso',null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
