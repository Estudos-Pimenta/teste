# Generated by Django 5.0.6 on 2024-07-12 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_alter_itemestoque_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='cleinte',
            new_name='cliente',
        ),
    ]