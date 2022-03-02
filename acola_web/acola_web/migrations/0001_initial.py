# Generated by Django 4.0.3 on 2022-03-02 20:54

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
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('senha', models.CharField(max_length=32)),
                ('nascimento', models.DateField()),
                ('admin', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
