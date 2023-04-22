from django.db import models
from django.urls import reverse


class UnitMeasure(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    code = models.CharField(max_length=64, unique=True, verbose_name="Код ОКЕИ")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ед. изм'
        verbose_name_plural = 'Ед. изм'
        ordering = ('name',)


class Supplier(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    inn = models.CharField(max_length=10, blank=True, verbose_name="ИНН")
    kpp = models.CharField(max_length=9, blank=True, verbose_name="КПП")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Наименование", db_index=True)
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Цена")
    receipt_date = models.DateField(blank=True, null=True, verbose_name='Дата поступления')
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE, verbose_name='Ед. изм.')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, verbose_name='Поставщик')

    def __str__(self):
        return f'({self.pk}) {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
