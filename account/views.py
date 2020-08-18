from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from django.http import HttpResponse
from product.views import *
import datetime

def index(request):
    if request.method == "POST":
        data = request.POST
        try:
            product = Product.objects.get(name__icontains=data['name'])
        except:
            product = "False"
        context = {'product': product}
        return render (request, 'search.html', context)
    category = Category.objects.all()
    product = Product.objects.all()
    present = datetime.datetime.now()
    offerenddate = datetime.datetime(2020, 11, 25, 8, 0, 0)
    countdown = offerenddate - present
    context = {'category': category, 'product': product, 'countdown': countdown}
    return render (request, 'base.html', context)
    
class Administrator (TemplateView):
    template_name = 'base_admin.html'
