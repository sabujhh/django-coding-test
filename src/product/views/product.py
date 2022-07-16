from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse

from product.models import *
from django.views import View
from django.core.paginator import Paginator
from product.filters import productListFilter


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(View):
    def get(self, request, *args, **kwargs):
        variant = Variant.objects.all()
        product = Product.objects.all()
        productVariant = ProductVariant.objects.all()
        productVariantPrice = ProductVariantPrice.objects.all()

        myFilter = productListFilter(request.GET, queryset=productVariantPrice)
        productVariantPrice = myFilter.qs
        
        p = Paginator(productVariantPrice, 5)
        page = request.GET.get('page')
        productList=p.get_page(page)
        nums = "a"*productList.paginator.num_pages

        context = {'variant' : variant, 'product':product, 'productVariant':productVariant, 
        'productVariantPrice':productVariantPrice, 'productList': productList, 'nums': nums, 'myFilter':myFilter}

        return render(request, 'products/list.html', context)
