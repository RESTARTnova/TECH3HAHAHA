from django.db import models

# Create your models here.
class Faults(models.Model):
    user = models.CharField('Пользователь', max_length=30, blank=True, null=True)
    rfid = models.CharField("Айди метки", max_length=16, blank=True, null=True)
    fault = models.CharField("Замечание", max_length=255, blank=True, null=True)
    tag = models.CharField("Содержимое метки", max_length=255, blank=True, null=True)
    data_time = models.DateField('Последний обход', blank=True, null=True)

    def __str__(self):
        return self.name

