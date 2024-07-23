# Generated by Django 5.0.7 on 2024-07-16 15:05

import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_bibita_prezzo'),
        ('client', '0009_remove_ordinedomicilio_modalita_ritiro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordineconsumazioneposto',
            name='token',
            field=models.UUIDField(default=uuid.UUID('9c98d5cc-399d-4966-a7c9-1066095fdc85')),
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='token',
            field=models.UUIDField(default=uuid.UUID('9c98d5cc-399d-4966-a7c9-1066095fdc85')),
        ),
        migrations.CreateModel(
            name='OrdineRitiroMezzogiorno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('data', models.DateField()),
                ('data_ordine', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(default=uuid.UUID('9c98d5cc-399d-4966-a7c9-1066095fdc85'))),
                ('status', models.IntegerField(choices=[(1, 'In Lavorazione'), (2, 'In Consegna'), (3, 'Consegnato')], default=2)),
                ('ora', models.TimeField(choices=[('12-12:15', '12-12:15'), ('12:15-12:30', '12:15-12:30'), ('12:30-12:45', '12:30-12:45'), ('12:45-13', '12:45-13'), ('13-13:15', '13-13:15'), ('13:15-13:30', '13:15-13:30'), ('13:30-13:45', '13:30-13:45')])),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.pizza')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrdineRitiroSera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('data', models.DateField()),
                ('data_ordine', models.DateTimeField(auto_now_add=True)),
                ('token', models.UUIDField(default=uuid.UUID('9c98d5cc-399d-4966-a7c9-1066095fdc85'))),
                ('status', models.IntegerField(choices=[(1, 'In Lavorazione'), (2, 'In Consegna'), (3, 'Consegnato')], default=2)),
                ('ora', models.TimeField(choices=[('17:45-18', '17:45-18'), ('18-18:15', '18-18:15'), ('18:15-18:30', '18:15-18:30'), ('18:30-18:45', '18:30-18:45'), ('18:45-19', '18:45-19'), ('19-19:15', '19-19:15'), ('19:15-19:30', '19:15-19:30'), ('19:30-19:45', '19:30-19:45'), ('19:45-20', '19:45-20'), ('20-20:15', '20-20:15'), ('20:15-20:30', '20:15-20:30'), ('20:30-20:45', '20:30-20:45'), ('20:45-21', '20:45-21'), ('21-21:15', '21-21:15'), ('21:15-21:30', '21:15-21:30'), ('21:30-21:45', '21:30-21:45'), ('21:45-22', '21:45-22'), ('22-22:15', '22-22:15'), ('22:15-22:30', '22:15-22:30'), ('22:30-22:45', '22:30-22:45'), ('22:45-23', '22:45-23'), ('23-23:15', '23-23:15'), ('23:15-23:30', '23:15-23:30'), ('23:30-23:45', '23:30-23:45')])),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.pizza')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='OrdineRitiro',
        ),
    ]