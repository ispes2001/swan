from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from product.views import *

# Create your views here.
def index(request):
    # template = loader.get_template('base.html')
    category = Category.objects.all()
    product = Product.objects.all()
    context = {'category': category, 'product': product}
    # return HttpResponse (template.render(context, request))
    return render (request, 'base.html', context)

def administrator(request):
    template = loader.get_template('base_admin.html')
    # return HttpResponse (template.render({}, request))
    return render (request, 'base_admin.html')