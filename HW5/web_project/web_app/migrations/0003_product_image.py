# Generated by Django 5.0.1 on 2024-02-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_rename_customer_id_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_photo', verbose_name='Image'),
        ),
    ]