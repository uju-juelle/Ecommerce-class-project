from django.shortcuts import render
from .models import *
# Create your views here.
def product_page(request):
    products = product.objects.all()
    context = {
        "allproducts": products
    }
    return render(request, "product.html", context)


def about(request):
    return render(request, "about.html")

def single_product_view(request,id):
    myproduct = product.objects.get(id=id)
    context = {
        "p": myproduct
    }
    return render(request,"products_detail.html", context)