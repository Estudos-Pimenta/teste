# Generated by Django 5.0.6 on 2024-07-12 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_rename_cleinte_pedido_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='id_usuario',
            new_name='id_sessao',
        ),
    ]