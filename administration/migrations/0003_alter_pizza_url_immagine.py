# Generated by Django 5.0.7 on 2024-07-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_rename_ingredienti_ingrediente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='url_immagine',
            field=models.URLField(blank=True, default=''),
        ),
    ]
