# Generated by Django 4.0.4 on 2022-05-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_images_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='photos/products'),
        ),
    ]
