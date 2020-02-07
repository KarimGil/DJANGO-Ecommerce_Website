from django.shortcuts import render
from .models import Item

# Create your views here.


def home_page(request):

    context = {

        'items': Item.objects.all()
    }

    return render(request, 'home-page.html', context)


def product_page(request):

    return render(request, 'product-page.html')


def checkout_page(request):

    return render(request, 'checkout-page.html')
