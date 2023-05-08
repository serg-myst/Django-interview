from django import template
from shop.models import ProductTags, Category

register = template.Library()


# https://django.fun/ru/articles/tutorials/select_related-i-prefetch_related-v-django/
@register.inclusion_tag('shop/includes/_product_tags.html', name='product_tags')
def get_product_tags(product):
    # tags = ProductTags.objects.prefetch_related('tags').all()
    tags = ProductTags.objects.filter(product=product)
    return {'tags': tags}


@register.inclusion_tag('shop/includes/_categories.html', name='categories')
def categories_tags(cat_selected=None):
    categories = Category.on_site.all()
    return {'categories': categories, 'cat_selected': cat_selected}
