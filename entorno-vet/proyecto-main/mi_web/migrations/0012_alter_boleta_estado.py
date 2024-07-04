# Generated by Django 5.0.6 on 2024-07-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0011_alter_boleta_estado_bloqueo_desbloqueo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('COMPLETADO', 'Completado'), ('ENVIO', 'Envio'), ('ALMACEN', 'Almacen')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
    ]
