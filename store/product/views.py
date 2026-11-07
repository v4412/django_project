from django.shortcuts import render
from .models import Product


def home_page(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})