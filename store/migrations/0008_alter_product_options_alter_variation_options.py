# Generated by Django 4.0.4 on 2022-05-25 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_options_alter_variation_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Publicacion', 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'Edicion - Producto', 'verbose_name_plural': 'Ediciones - Productos'},
        ),
    ]