from django.db import models
from django.urls import reverse
from django.contrib.sites.models import Site  # создаем поле сайт
from django.contrib.sites.managers import CurrentSiteManager  # для фильтрации моделей по сайту

from django.db.models import Manager


# Реализуем команду (метод), который можно будет добавлять в запросы
# Наследуемся от стандартного Queryset
class DeletedQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(deleted=False)


class DeletedManager(CurrentSiteManager, Manager):
    def get_queryset(self):  # Данным подходом мы сразу меняем запрос
        return super().get_queryset().filter(deleted=False)

    # def get_queryset(self):  # Данным подходом мы реализуем метод not_deleted()
    #    return DeletedQuerySet(self.model, using=self._db)


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
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    # on_site = CurrentSiteManager('site')  # Для связи модели с сайтом
    deleted = models.BooleanField(default=False, null=False)  # Для тестирования кастомного менеджера запросов

    # Сразу переопределим queryset с учетом sites. DeletedManager(CurrentSiteManager, Manager)
    objects = DeletedManager()

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
