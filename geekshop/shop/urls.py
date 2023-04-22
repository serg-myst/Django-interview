from django.urls import path, re_path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),

]