from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    # return HttpResponse("Hello, World. You are at home page.")
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("Hello, World. You are at about page.")

def contact(request):
    return HttpResponse("Hello, World. You are at contact page.")