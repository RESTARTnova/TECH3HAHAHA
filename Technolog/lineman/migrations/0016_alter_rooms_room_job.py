# Generated by Django 4.2.1 on 2024-02-29 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineman', '0015_alter_rooms_room_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_job',
            field=models.ManyToManyField(to='lineman.actions'),
        ),
    ]
