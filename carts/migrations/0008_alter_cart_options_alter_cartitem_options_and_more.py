# Generated by Django 4.0.4 on 2022-05-25 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
    ]