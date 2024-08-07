# Generated by Django 5.0.7 on 2024-07-16 15:33

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_bibita_prezzo'),
        ('client', '0011_alter_ordineconsumazioneposto_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordineconsumazioneposto',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.bibita'),
        ),
        migrations.AddField(
            model_name='ordinedomicilio',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.bibita'),
        ),
        migrations.AddField(
            model_name='ordineritiromezzogiorno',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.bibita'),
        ),
        migrations.AddField(
            model_name='ordineritirosera',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.bibita'),
        ),
        migrations.AlterField(
            model_name='ordineconsumazioneposto',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.pizza'),
        ),
        migrations.AlterField(
            model_name='ordineconsumazioneposto',
            name='token',
            field=models.UUIDField(default=uuid.UUID('e8c750c4-ff4e-4158-9367-1fdc931cd56f')),
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.pizza'),
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='token',
            field=models.UUIDField(default=uuid.UUID('e8c750c4-ff4e-4158-9367-1fdc931cd56f')),
        ),
        migrations.AlterField(
            model_name='ordineritiromezzogiorno',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.pizza'),
        ),
        migrations.AlterField(
            model_name='ordineritiromezzogiorno',
            name='token',
            field=models.UUIDField(default=uuid.UUID('e8c750c4-ff4e-4158-9367-1fdc931cd56f')),
        ),
        migrations.AlterField(
            model_name='ordineritirosera',
            name='pizza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.pizza'),
        ),
        migrations.AlterField(
            model_name='ordineritirosera',
            name='token',
            field=models.UUIDField(default=uuid.UUID('e8c750c4-ff4e-4158-9367-1fdc931cd56f')),
        ),
    ]
