from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product, Category
from django.urls import reverse
from django.contrib import messages
import sweetify

def category(request):
    template = loader.get_template('category/category_display.html')
    category = Category.objects.all()
    return HttpResponse (template.render({'category': category}, request))



def category_add(request):
    template = loader.get_template('category/category_add.html')
    # category = Category.objects.all()
    if request.method == 'POST':
        data=request.POST
        name = data ['name']
        slug = data ['slug']
        # chck = Category.objects.filter(slug=slug)
        objt, created = Category.objects.get_or_create(name = name, defaults = {'slug' : slug} )
        if created==False:
            # obj_exists = True
            # messages.warning(request, 'You are trying to enter duplicate name!!!')
            msg = sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
            context = {'msg' :msg}
            return HttpResponse (template.render(context, request))
        # obj = Category.objects.create(name = name, slug = slug)
        return HttpResponseRedirect (reverse('category'))
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


