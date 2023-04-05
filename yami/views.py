from django.shortcuts import render, get_object_or_404
from yami.models import Product
# Create your views here.


def index(request):
    return render(request, "index.html")




def checkout(request):
    return render(request, "checkout.html")


def shopingcart(request):
    return render(request, "shopingcart.html")


def shops(request):
    pro = Product.objects.filter(is_pub=True)[:]
    return render(request, "shops.html", {
        'products': pro
        })


def detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'shop-single.html', {
        'p': item
        })


def contact(request):
    return render(request, "contact.html")
