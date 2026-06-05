from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("visit/", views.visit, name='visit'),
    path("products/", views.product_list, name='product_list'),
]