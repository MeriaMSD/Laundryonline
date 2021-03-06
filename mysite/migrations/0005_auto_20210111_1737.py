# Generated by Django 3.1.5 on 2021-01-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210111_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product_order',
            new_name='order_product',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, choices=[('1', 'Laundry Service'), ('2', 'Dry Cleaning & Ironed Laundry'), ('3', 'Home & Bedding')], default='1', max_length=1),
        ),
    ]
