# Generated by Django 5.0.7 on 2024-07-22 07:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_remove_ordinedomicilio_bibita_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordine',
            name='token',
            field=models.UUIDField(default=uuid.UUID('d45867fb-e54d-42d7-83d1-20b0d9ccd67e')),
        ),
    ]
