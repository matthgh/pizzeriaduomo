# Generated by Django 5.0.7 on 2024-07-12 20:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_ordine_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='token',
            field=models.UUIDField(default=uuid.UUID('ef4c4533-a3ea-44e3-a2d1-87ecebb4b675')),
        ),
    ]
