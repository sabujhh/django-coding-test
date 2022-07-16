import django_filters

from .models import *

class productListFilter(django_filters.FilterSet):
    model = ProductVariantPrice
    fields = '__all__'