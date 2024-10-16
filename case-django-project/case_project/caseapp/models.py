from django.db import models

# Create your models here.


class RegModel(models.Model):
    date_time = models.CharField('Дата-время', max_length=50, blank=True)
    quantity_adult = models.IntegerField('Количество взрослых билетов', blank=True)
    quantity_kids = models.IntegerField('Количество детских билетов', blank=True)
    price = models.CharField('Цена', max_length=50, blank=True)
