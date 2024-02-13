from django.db import models

# Create your models here.
class Factoryes(models.Model):
    name = models.CharField('Завод', max_length=255)
   
    def __str__(self):
        return self.name
    
class Departaments(models.Model):
    factory = models.ForeignKey(Factoryes, on_delete=models.CASCADE)
    name = models.CharField('Цех', max_length=255)
  
    def __str__(self):
        return self.name
    
class Aggregates(models.Model):
    departament = models.ForeignKey(Departaments,on_delete=models.CASCADE)
    name = models.CharField('Агрегат', max_length=255)
    inv_number = models.IntegerField('Инвентаризационный номер',blank=True, null=True)
    place_of_state = models.CharField('Место установки', max_length=1023)
    date_of_last_TS = models.DateField('Последнее ТО', blank=True, null=True)
    date_of_last_TR = models.DateField('Последнее ТР',blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
   
    def __str__(self):
        return self.name

class Machines(models.Model):
    aggregat = models.ForeignKey(Aggregates, on_delete=models.CASCADE)
    rfid = models.CharField("RFID ID",max_length=16, blank=True, null=True)
    name = models.CharField('Название системы', max_length=255)
    location = models.CharField("Расположение", max_length=1023)
    date_of_last_TS = models.DateField('Последнее ТО', blank=True, null=True)
    date_of_last_TR = models.DateField('Последнее ТР',blank=True, null=True)
    running_time = models.IntegerField("Время наработки",blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Nodes(models.Model):
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE)
    name = models.CharField('Узел', max_length=255)
    date_of_last_TS = models.DateField('Последнее ТО', blank=True, null=True)
    date_of_last_TR = models.DateField('Последнее ТР',blank=True, null=True)
    running_time = models.IntegerField("Время наработки",blank=True,null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name

class Elements(models.Model):
    element = models.ForeignKey(Nodes, on_delete=models.CASCADE)
    name = models.CharField('Элемент', max_length=255)
    specification = models.CharField("Спецификация", max_length=255)
    date_of_last_TS = models.DateField('Последнее ТО', blank=True, null=True)
    date_of_last_TR = models.DateField('Последнее ТР',blank=True, null=True)
    running_time = models.IntegerField("Время наработки",blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Details(models.Model):
    detail = models.ForeignKey(Elements, on_delete=models.CASCADE)
    name = models.CharField('Деталь', max_length=255)
    specification = models.CharField("Спецификация", max_length=255)
    date_of_last_TS = models.DateField('Последнее ТО', blank=True, null=True)
    date_of_last_TR = models.DateField('Последнее ТР',blank=True, null=True)
    running_time = models.IntegerField("Время наработки",blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name

