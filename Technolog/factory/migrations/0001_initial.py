# Generated by Django 4.2.1 on 2023-12-25 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Агрегат')),
                ('inv_number', models.IntegerField(blank=True, null=True, verbose_name='Инвентаризационный номер')),
                ('place_of_state', models.CharField(max_length=1023, verbose_name='Место установки')),
                ('date_of_last_TS', models.DateField(blank=True, null=True, verbose_name='Последнее ТО')),
                ('date_of_last_TR', models.DateField(blank=True, null=True, verbose_name='Последнее ТР')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name_plural': 'Агрегаты',
            },
        ),
        migrations.CreateModel(
            name='Factoryes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Завод')),
            ],
            options={
                'verbose_name_plural': 'Заводы',
            },
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(blank=True, max_length=16, null=True, verbose_name='RFID ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название системы')),
                ('location', models.CharField(max_length=1023, verbose_name='Расположение')),
                ('date_of_last_TS', models.DateField(blank=True, null=True, verbose_name='Последнее ТО')),
                ('date_of_last_TR', models.DateField(blank=True, null=True, verbose_name='Последнее ТР')),
                ('running_time', models.IntegerField(blank=True, null=True, verbose_name='Время наработки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('aggregat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.aggregates')),
            ],
            options={
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Узел')),
                ('date_of_last_TS', models.DateField(blank=True, null=True, verbose_name='Последнее ТО')),
                ('date_of_last_TR', models.DateField(blank=True, null=True, verbose_name='Последнее ТР')),
                ('running_time', models.IntegerField(blank=True, null=True, verbose_name='Время наработки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.machines')),
            ],
            options={
                'verbose_name_plural': 'Узлы',
            },
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Элемент')),
                ('specification', models.CharField(max_length=255, verbose_name='Спецификация')),
                ('date_of_last_TS', models.DateField(blank=True, null=True, verbose_name='Последнее ТО')),
                ('date_of_last_TR', models.DateField(blank=True, null=True, verbose_name='Последнее ТР')),
                ('running_time', models.IntegerField(blank=True, null=True, verbose_name='Время наработки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.nodes')),
            ],
            options={
                'verbose_name_plural': 'Элементы',
            },
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Деталь')),
                ('specification', models.CharField(max_length=255, verbose_name='Спецификация')),
                ('date_of_last_TS', models.DateField(blank=True, null=True, verbose_name='Последнее ТО')),
                ('date_of_last_TR', models.DateField(blank=True, null=True, verbose_name='Последнее ТР')),
                ('running_time', models.IntegerField(blank=True, null=True, verbose_name='Время наработки')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.elements')),
            ],
            options={
                'verbose_name_plural': 'Детали',
            },
        ),
        migrations.CreateModel(
            name='Departaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Цех')),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.factoryes')),
            ],
            options={
                'verbose_name_plural': 'Цеха',
            },
        ),
        migrations.AddField(
            model_name='aggregates',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.departaments'),
        ),
    ]
