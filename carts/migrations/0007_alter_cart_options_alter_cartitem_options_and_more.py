# Generated by Django 4.0.4 on 2022-05-25 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_cartitem_variations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Item del pedido', 'verbose_name_plural': 'Items del pedido'},
        ),
        migrations.AlterModelTable(
            name='cart',
            table=None,
        ),
    ]