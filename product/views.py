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
        sweetify.success(request, 'You did it', text='Category Successfully added', persistent='Hell yeah')        
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
        category_id = data ['category']
        name = data ['name']
        slug = data ['slug']
        # image = data ['image']
        description = data ['description']
        price = data ['price']
        available = bool(data ['available'])
        # available = False
        # if available == False:
        #     msg = sweetify.success(request, 'You did it', text="message won't be displayed to customers", persistent='Hell yeah')
        #     context = {'msg' : msg}
            # return HttpResponse (template.render(context, request))
        # print (available)
        product, created  = Product.objects.get_or_create(name=name,category_id=category_id,slug = slug, defaults = {'description': description, 'price' : price, 'available': available})
        if created == False:
            msg = sweetify.success(request, 'You did it', text='Duplicate product message', persistent='Hell yeah')
            return HttpResponse (template.render({}, request))
        sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
        return HttpResponseRedirect (reverse('product'))
    context = {
        'categories':Category.objects.all()
    }
    return HttpResponse (template.render(context, request))


