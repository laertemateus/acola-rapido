# Generated by Django 4.0.3 on 2022-03-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acola_web', '0002_auto_20220302_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
