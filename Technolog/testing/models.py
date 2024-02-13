from django.db import models

# Create your models here.


class ForeignKeyTest(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Верхняя таблица'

class ForeignKeyTestF(models.Model):
    foreign_key_test = models.ForeignKey(ForeignKeyTest, on_delete=models.CASCADE)
    name_f = models.CharField(max_length=255)
    number_f = models.IntegerField()

    def __str__(self):
        return self.name_f
    
    class Meta:
        verbose_name_plural = 'Нижняя таблица'
