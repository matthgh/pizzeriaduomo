# Generated by Django 5.0.7 on 2024-07-12 20:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='token',
            field=models.UUIDField(default=uuid.UUID('7f5d0756-5149-40b9-9b27-e94ed87ca971')),
        ),
    ]
