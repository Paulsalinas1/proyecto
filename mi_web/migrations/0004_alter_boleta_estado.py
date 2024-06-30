# Generated by Django 5.0.6 on 2024-06-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0003_alter_boleta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('COMPLETADO', 'Completado'), ('ENVIO', 'Envio'), ('ALMACEN', 'Almacen'), ('CANCELADO', 'Cancelado')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
    ]
