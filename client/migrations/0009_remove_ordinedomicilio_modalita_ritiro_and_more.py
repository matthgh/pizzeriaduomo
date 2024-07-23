# Generated by Django 5.0.7 on 2024-07-16 14:23

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_bibita_prezzo'),
        ('client', '0008_alter_ordineritiro_token_ordinedomicilio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordinedomicilio',
            name='modalita_ritiro',
        ),
        migrations.RemoveField(
            model_name='ordineritiro',
            name='modalita_ritiro',
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='token',
            field=models.UUIDField(default=uuid.UUID('afda859f-1a41-44d9-b59a-5ce65ca80c5f')),
        ),
        migrations.AlterField(
            model_name='ordineritiro',
            name='token',
            field=models.UUIDField(default=uuid.UUID('afda859f-1a41-44d9-b59a-5ce65ca80c5f')),
        ),
        migrations.CreateModel(
            name='OrdineConsumazionePosto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('data', models.DateField()),
                ('data_ordine', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(default=uuid.UUID('afda859f-1a41-44d9-b59a-5ce65ca80c5f'))),
                ('status', models.IntegerField(choices=[(1, 'In Lavorazione'), (2, 'In Consegna'), (3, 'Consegnato')], default=2)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.pizza')),
            ],
        ),
    ]