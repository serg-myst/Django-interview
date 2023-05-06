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
    name = models.CharField(max_length=64, verbose_name="Наименование")
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    inn = models.CharField(max_length=10, blank=True, verbose_name="ИНН")
    kpp = models.CharField(max_length=9, blank=True, verbose_name="КПП")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Категория", db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name="Тэг", db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименование", db_index=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Цена")
    receipt_date = models.DateField(blank=True, null=True, verbose_name='Дата поступления')
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE, verbose_name='Ед. изм.')
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, verbose_name='Поставщик')
    tags = models.ManyToManyField(Tag, verbose_name='Разделы', blank=True, through='Producttags')

    def __str__(self):
        return f'({self.pk}) {self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)


class ProductTags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.product}) {self.tag}'

    class Meta:
        verbose_name = 'Разделы товаров'
        verbose_name_plural = 'Разделы товаров'
