from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from shop.models import Product, Supplier, UnitMeasure
from shop.forms import ProductForm
from django.template.loader import render_to_string
from django.http import JsonResponse


class ShopHome(ListView):
    model = Product
    template_name = 'shop/goods_list.html'
    context_object_name = 'products'
    allow_empty = True


class ShopCat(ListView):
    model = Product
    template_name = 'shop/goods_list.html'
    context_object_name = 'products'
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('cat').filter(cat__id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = self.kwargs['pk']
        context = context
        return context


'''
class ProductCreateView(CreateView):
    """Создание товара"""
    model = Product
    form_class = ProductForm
    template_name = 'shop/good_create.html'
    success_url = '/'

    # Здесь можно что-то добавить в создаваемый объект

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)
'''


def create_product(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        form = ProductForm(request.POST)
        if request.method == 'POST':
            return save_good_form(request, form, '')
        else:
            return save_good_form(request, form, 'shop/good_create.html')


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        data['form_is_valid'] = True
        products = Product.objects.all()
        data['html_good_list'] = render_to_string('shop/includes/_partial_goods_list.html', {
            'products': products
        })
    else:
        data['form_is_valid'] = False
        context = {'form': form}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
