from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product, Category
from django.urls import reverse

def category(request):
    template = loader.get_template('category/category_display.html')
    category = Category.objects.all()
    return HttpResponse (template.render({'category': category}, request))

def category_add(request):
    template = loader.get_template('category/category_add.html')
    # category = Category.objects.all()
    return HttpResponse (template.render({}, request))


def product(request):
    template = loader.get_template('product/product.html')
    product = Product.objects.all()
    return HttpResponse (template.render({'product': product}, request))

def add_product(request):
    template = loader.get_template('product/add_product.html')
    if request.method == "POST":
        data = request.POST
        # print (data)
        category = data ['name']
        name = data ['name']
        slug = data ['slug']
        # image = data ['image']
        description = data ['description']
        price = data ['price']
        available = data ['available']
        product = Product.objects.create(name=name, slug = slug, description = description, price = price, available = available )
        return HttpResponseRedirect (reverse('product'))
    return HttpResponse (template.render({}, request))


