# Generated by Django 4.2.1 on 2023-09-10 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_rename_costo_compras_total_compra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compras',
            old_name='servicio',
            new_name='servicios',
        ),
    ]
