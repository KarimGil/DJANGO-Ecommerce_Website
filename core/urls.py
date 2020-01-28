from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('product_page', views.product_page, name='product_page'),
    path('checkout_page', views.checkout_page, name='checkout_page'),

]
