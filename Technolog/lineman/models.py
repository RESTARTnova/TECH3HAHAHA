from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Durability(models.Model):
    dur_name = models.CharField('Состояние метки', unique=True)
    class Meta:
        verbose_name_plural = "Состояние меток"
    def __str__(self):
        return self.dur_name

class Logs(models.Model):
    logl = models.CharField('Лог')
    timel = models.CharField('Время')
    class Meta:
        verbose_name_plural = 'Логи'
    def __str__(self):
        return self.timel

class NFC(models.Model):
    nfc_code = models.CharField("Код метки",max_length=18,unique=True)
    nfc_dur = models.ForeignKey(Durability, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Метки'
    def __str__(self):
        return self.nfc_code

class Actions(models.Model):
    name_action = models.CharField('Название действия', blank=True, null=True, unique=True)
    class Meta:
        verbose_name_plural = 'Действия'
    def __str__(self):
        return self.name_action

class Job_titles(models.Model):
    job_name = models.CharField('Название должности', blank=True, null=True, unique=True)
    job_action = models.ManyToManyField(Actions,related_name='job_action')
    class Meta:
        verbose_name_plural = "Должности"
        verbose_name = "Должность"
    def __str__(self):
        return self.job_name

class Users(models.Model):
    login = models.CharField('Логин', max_length=128, unique=True)
    password = models.CharField('Пароль', max_length=128, )
    job_title = models.ForeignKey(Job_titles, on_delete=models.CASCADE, blank=True, null=True)
    nfc_id = models.ForeignKey(NFC, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return self.login
    
class ActionsRoom(models.Model):
    name_r = models.CharField(blank=False,null=False)
    remark_r = models.CharField(blank=True,null=False)
    class Meta:
        verbose_name = 'action room'
    def __str__(self):
        return str(self.pk)

class RoomsReport(models.Model):
    room_r = models.CharField('Название комнаты',blank=True,null=False)
    actions_r = models.ManyToManyField(ActionsRoom)
    class Meta:
        verbose_name = 'room report'
    def __str__(self):
        return str(self.pk)

class ReportsRoom(models.Model):
    rep_name = models.CharField('Название профессии')
    rep_start_time = models.DateTimeField('Время начала', blank=True, null=True)
    rep_stop_time = models.DateTimeField('Время конца', blank=True, null=True)
    rep_string = models.CharField('Excel',blank=True, null=True)
    rep_rooms = models.ManyToManyField(RoomsReport)
    rep_logs = models.ManyToManyField(Logs)
    class Meta:
        verbose_name_plural = "Отчёты участков"
    def __str__(self):
        return str(self.rep_start_time).split('.')[0] + '-' + str(self.rep_stop_time).split('.')[0] + '/' + str(self.rep_name)

class Rooms(models.Model):
    room_name = models.CharField('Название участка', unique=True)
    room_nfcID = models.ForeignKey(NFC, on_delete=models.CASCADE, blank=True, null=True)
    room_action = models.ManyToManyField(Actions, related_name='room_action')
    class Meta:
        verbose_name_plural = "Участки"
    def __str__(self):
        return self.room_name

