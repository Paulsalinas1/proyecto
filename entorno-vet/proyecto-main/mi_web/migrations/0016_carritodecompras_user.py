# Generated by Django 5.0.6 on 2024-06-26 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_web', '0015_remove_carritodecompras_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritodecompras',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
