# Generated by Django 4.2.1 on 2024-01-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineman', '0002_alter_users_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Пароль'),
        ),
    ]
