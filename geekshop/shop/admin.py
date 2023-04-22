from django.contrib import admin
from .models import Product, Supplier, UnitMeasure


class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = ('id', 'name', 'full_name', 'unit_measure', 'supplier')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'full_name', 'price')
    list_filter = ('receipt_date',)
    # readonly_fields = ('',)


class SupplierAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = ('id', 'name', 'full_name', 'inn', 'kpp')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'full_name', 'inn', 'kpp')


class UnitMeasureAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_display = ('id', 'code', 'name', 'full_name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'code',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(UnitMeasure, UnitMeasureAdmin)
