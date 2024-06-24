# Generated by Django 5.0.6 on 2024-06-24 00:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0007_alter_tarjeta_tarjeta_de_credito'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarjeta',
            name='uusuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
    ]
