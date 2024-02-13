from datetime import timedelta
from email.policy import default
from django.db import models
from factory.models import Machines, Nodes, Elements, Details

 # Create your models here.

class Shutdown(models.Model):
    date_begin = models.DateTimeField('Начало простоя')
    date_end = models.DateTimeField('Окончание простоя')
    interval = models.DurationField('продолжительность', blank=True, null=True)
    agregate_name = models.CharField('Название агрегата', max_length=255) 
    flag_classification = models.BooleanField('Флаг', default=False, blank=True) # класифицирован ли простой
    class_shutdown = models.ForeignKey("ClassShutdown", on_delete=models.CASCADE, blank=True, null=True)
    type_shutdown = models.ForeignKey("TypeShutdown", on_delete=models.CASCADE, blank=True, null=True)
    factor_shutdown = models.ForeignKey("FactorShutdown", on_delete=models.CASCADE, blank=True, null=True)
    commentary = models.TextField("Примечание", blank=True)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE, blank=True, null=True)
    node = models.ForeignKey(Nodes, on_delete=models.CASCADE, blank=True, null=True)
    element = models.ForeignKey(Elements, on_delete=models.CASCADE, blank=True, null=True)
    detail = models.ForeignKey(Details, on_delete=models.CASCADE, blank=True, null=True)
    href_documentation = models.CharField('Связанные документы', blank=True, null=True)



    def __str__(self):
        return f"{self.agregate_name} с {self.date_begin} по {self.date_end} "
        # return '__all__'

class ClassShutdown(models.Model):
    class_shutdown = models.CharField("Вид простоя", max_length=255)

    def __str__(self):
        return self.class_shutdown
    
    class Meta:
        verbose_name_plural = 'Виды простоев'

class TypeShutdown(models.Model):
    class_shutdown = models.ForeignKey(ClassShutdown, on_delete=models.CASCADE)
    type_shutdown = models.CharField("Тип простоя", max_length=255)
    flag_dr_and_ts = models.BooleanField("ЦРиТО", default=False) #этот флаг должен включаться если тип простоя будет зависеть от оборудования
                                                                 # и подключать форму формирования единицы оборудования, которая вышла из строя

    def __str__(self):
        return self.type_shutdown
    
    class Meta:
        verbose_name_plural = 'Типы простоев'


class FactorShutdown(models.Model):
    type_shutdown = models.ForeignKey(TypeShutdown, on_delete=models.CASCADE)
    factor_shutdown = models.CharField("Фактор простоя", max_length=255)

    def __str__(self):
        return self.factor_shutdown
    
    class Meta:
        verbose_name_plural = 'Факторы простоев'