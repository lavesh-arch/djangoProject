from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def visit(request):
    return Response({"message": "Welcome to the E-commerce API!"})

@api_view(['GET'])
def product_list(request):
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Smartphone", "price": 499.99},
        {"id": 3, "name": "Headphones", "price": 199.99},
    ]
    return Response(products)
