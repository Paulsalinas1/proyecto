# Generated by Django 5.0.6 on 2024-07-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0023_alter_boleta_estado_alter_reclamo_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('ENVIO', 'Envio'), ('ALMACEN', 'Almacen'), ('COMPLETADO', 'Completado')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='tipo',
            field=models.CharField(choices=[('SERVICIO', 'Servicio'), ('OTRO', 'Otro'), ('PRODUCTO', 'Producto')], max_length=20, verbose_name='Tipo de reclamo'),
        ),
    ]