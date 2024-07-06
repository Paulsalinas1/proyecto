# Generated by Django 5.0.6 on 2024-07-04 23:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0013_alter_boleta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('ENVIO', 'Envio'), ('ALMACEN', 'Almacen'), ('COMPLETADO', 'Completado'), ('CANCELADO', 'Cancelado')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('SERVICIO', 'Servicio'), ('OTRO', 'Otro'), ('PRODUCTO', 'Producto')], max_length=20, verbose_name='Tipo de reclamo')),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_PROCESO', 'En proceso'), ('RESUELTO', 'Resuelto')], default='PENDIENTE', max_length=20, verbose_name='Estado del reclamo')),
                ('descripcion', models.TextField(verbose_name='Descripción del reclamo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
