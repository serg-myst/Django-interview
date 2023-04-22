from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from shop.models import Product, Supplier, UnitMeasure
from shop.forms import ProductForm


class ShopHome(ListView):
    model = Product
    template_name = 'shop/goods_list.html'
    context_object_name = 'products'
    allow_empty = False


class ProductCreateView(CreateView):
    """Создание товара"""

    model = Product
    form_class = ProductForm
    template_name = 'shop/good_create.html'
    success_url = '/'

    # Здесь можно что-то добавить в создаваемый объект
    '''
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)
    '''
