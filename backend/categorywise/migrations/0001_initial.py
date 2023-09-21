# Generated by Django 4.1.4 on 2023-09-14 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_numofstocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorywise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(default='', max_length=255, null=True)),
                ('categoryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
        ),
    ]
