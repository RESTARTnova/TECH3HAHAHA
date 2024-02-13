from django.db import models
from django.utils import timezone

# Create your models here.
class Systems(models.Model):
    name_system = models.CharField('Название системы', blank=True, null=True)
    descriptions_system = models.TextField('Описание системы', blank=True, null=True)
    nfc_id_system = models.CharField('Метка системы', blank=True, null=True, max_length=15, unique=True)
    class Meta:
        verbose_name_plural = "Системы"
    def __str__(self):
        return self.name_system
    
class Bypass(models.Model):
    name_bypass = models.CharField('Название обхода', blank=True, null=True, unique=True)
    action_bypass = models.CharField('Действие во время обхода', blank=True, null=True)
    #list_systems = models.ManyToManyField('Список систем', Systems, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Пути обхода"
    def __str__(self):
        return self.name_bypass

class Job_titles(models.Model):
    job_name = models.CharField('Название должности', blank=True, null=True, unique=True)
    class Meta:
        verbose_name_plural = "Должности"
    def __str__(self):
        return self.job_name

class Users(models.Model):
    login = models.CharField('Логин', max_length=128, unique=True)
    password = models.CharField('Пароль', max_length=128, )
    bypass = models.ForeignKey(Bypass, on_delete=models.CASCADE, blank=True, null=True)
    job_title = models.ForeignKey(Job_titles, on_delete=models.CASCADE, blank=True, null=True)
    nfc_id = models.CharField('Личная метка', max_length=15, blank=True, null=True, unique=True)
    class Meta:
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return self.login

class Warning(models.Model):
    name_warn = models.CharField('Название неисправности', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Неисправности"
    def __str__(self):
        return self.name_warn
    
class Reports(models.Model):
    rep_name = models.CharField('Название отчёта', unique=True)
    rep_login = models.CharField('Логин обходчика', blank=True, null=True)
    rep_start_time = models.DateTimeField('Время начала', blank=True, null=True, default=timezone.now)
    rep_stop_time = models.DateTimeField('Время конца', blank=True, null=True, auto_now_add=True)
    rep_passed = models.CharField('Пройдено меток', blank=True, null=True, default="0/0")
    rep_remark = models.BooleanField('Наличие замечания')
    #rep_note = models.ManyToManyField('Замечание', Warning, blank=True, null=True)
    rep_explanation = models.CharField('Пояснение к замечанию', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Отчёты"
    def __str__(self):
        return self.rep_name