# Generated by Django 3.1.5 on 2021-01-11 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210111_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['order_date']},
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_store',
        ),
    ]
