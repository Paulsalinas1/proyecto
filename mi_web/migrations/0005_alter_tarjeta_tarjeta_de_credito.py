# Generated by Django 5.0.6 on 2024-06-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0004_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='tarjeta_de_credito',
            field=models.IntegerField(max_length=16, unique=True, verbose_name='numero tarjeta'),
        ),
    ]
