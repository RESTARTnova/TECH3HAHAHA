# Generated by Django 4.2.1 on 2024-01-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(max_length=128, unique=True, verbose_name='Логин'),
        ),
    ]
