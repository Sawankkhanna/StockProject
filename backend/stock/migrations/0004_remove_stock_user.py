# Generated by Django 4.1.4 on 2023-08-25 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stock_postmarketchangepercent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='user',
        ),
    ]
