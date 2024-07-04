# Generated by Django 5.0.6 on 2024-06-30 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0007_alter_boleta_carritodecompra_alter_boleta_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(choices=[('CANCELADO', 'Cancelado'), ('ALMACEN', 'Almacen'), ('ENVIO', 'Envio'), ('COMPLETADO', 'Completado')], default='ALMACEN', max_length=20, verbose_name='estado'),
        ),
        migrations.CreateModel(
            name='ProductoBoleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_web.boleta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mi_web.producto')),
            ],
        ),
    ]