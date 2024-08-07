# Generated by Django 5.0.7 on 2024-07-16 15:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_bibita_prezzo'),
        ('client', '0012_ordineconsumazioneposto_bibita_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordineconsumazioneposto',
            name='token',
            field=models.UUIDField(default=uuid.UUID('6773aae4-4f80-4b28-8897-2dadf0c80281')),
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='token',
            field=models.UUIDField(default=uuid.UUID('6773aae4-4f80-4b28-8897-2dadf0c80281')),
        ),
        migrations.AlterField(
            model_name='ordineritiromezzogiorno',
            name='token',
            field=models.UUIDField(default=uuid.UUID('6773aae4-4f80-4b28-8897-2dadf0c80281')),
        ),
        migrations.AlterField(
            model_name='ordineritirosera',
            name='token',
            field=models.UUIDField(default=uuid.UUID('6773aae4-4f80-4b28-8897-2dadf0c80281')),
        ),
        migrations.CreateModel(
            name='ConsumazioneBibite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.IntegerField(default=1)),
                ('bibita', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.bibita')),
            ],
        ),
        migrations.AlterField(
            model_name='ordineconsumazioneposto',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.consumazionebibite'),
        ),
        migrations.AlterField(
            model_name='ordinedomicilio',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.consumazionebibite'),
        ),
        migrations.AlterField(
            model_name='ordineritiromezzogiorno',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.consumazionebibite'),
        ),
        migrations.AlterField(
            model_name='ordineritirosera',
            name='bibita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.consumazionebibite'),
        ),
    ]
