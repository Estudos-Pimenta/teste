# Generated by Django 5.0.7 on 2024-07-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0010_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]