from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('Category', 'id')
    cats = {item['Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return  render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("Contact page")

def tracker(request):
    return HttpResponse("Tracking Status")

def productView(request):
    return HttpResponse("Product view")

def search(request):
    return HttpResponse("Search")

def checkout(request):
    return HttpResponse("Checkout Page")