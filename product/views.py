from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product, Category
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import sweetify
from django.views import View
from django.views.generic import ListView, CreateView
from .forms import *
from django.core.files.storage import FileSystemStorage


from django.views.generic import TemplateView

class CategoryView(ListView):
    template_name = 'category/category_display.html'
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs ['extra'] = "This is Extra from method override"
        kwargs ['category'] = self.get_queryset()
        return kwargs

class storeProduct (TemplateView):
    template_name = 'product/store.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        params = self.request.GET
        # if request.method =='POST':
        #     filter_price1 = self.request.GET.get('min_price')
        #     filter_price2 = self.request.GET.get('max_price')
        #     print (filter_price2)
        #     if filter_price1 =='':
        #         filter_price1=0
        # if filter_price2=='':
        #     my_products=Product.objects.filter(price__range(filter_price1,filter_price2['max_price']))
        # my_products = Product.objects.filter(price__range=(filter_price1,filter_price2))
        category = Category.objects.get(id=params['category_id'])
        filtered_products = category.products.all()
        kwargs['product']=filtered_products
        return kwargs

# def filter_price(request): 
#     if 'min_price' in request.GET:
        # filter_price1 = request.GET.get('min_price')
        # filter_price2 = request.GET.get('max_price')
        # if filter_price1 =='':
        #     filter_price1=0
        # if filter_price2=='':
        #     filter_price2=Product.objects.all().aggregate(Max('price'))
        #     my_products=Product.objects.filter(price__range(filter_price1,filter_price2['max_price']))
#         my_products = Product.objects.filter(price__range=(filter_price1,filter_price2))
#         context = { "products":my_products}
#     return render(request,"pricefilter.html",context)


def category_add(request):
    form = AddCategoryForm()
    context = {'form': form}
    if request.method =='POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'You did it', text='Category Successfully added', persistent='Hell yeah')        
            return redirect ('category')
        context = {'form': form}
        return render (request, 'category/category_add.html', context)
    return render (request, 'category/category_add.html', context)


class ProductView (ListView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'product'

class ProductAddView (CreateView):
    template_name = 'product/add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy ('product:product')

def add_product(request):
    form = AddProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            image = Product.objects.filter(image)         
            form.save()
            sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
            return redirect ('product:product')
        context = {'form': form}
        return render (request, 'product/add_product.html', context)
    return render (request, 'product/add_product.html', context)

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    form = AddProductForm(instance=product)
    context = {'form': form, 'update': True, 'categories': categories}
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'You did it', text='Product Successfully Updated', persistent='Hell yeah')        
            return redirect ('product')
        context = {'form': form, 'update': True, 'categories': categories}
        return render (request, 'product/add_product.html', context)        
    return render (request, 'product/add_product.html', context)


def delete_product (request, id):
    product = get_object_or_404 (Product, id=id)
    product.delete()
    sweetify.success(request, 'You did it', text='Product deleted successfully', persistent='Hell yeah')        
    return redirect ('product')

def category_update(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        category.name = data ['name']
        category.slug = data ['slug']
        category.save()
        sweetify.success(request, 'You did it', text='Updated Successfully', persistent='Hell yeah')        
        return redirect ('category')
    context = {'category': category, 'update': True}
    return render (request, 'category/category_add.html', context)



def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    sweetify.success(request, 'You did it', text='Category deleted successfully', persistent='Hell yeah')        
    return redirect ('category')


def category_group(request, id):
    group = get_object_or_404 (Category, id=id)
    context = group.products.all()
    try:
        title = group.products.all()[id].category
    except:
        title = 'No products available'
    context = {'group':context, 'title': title}
    return render (request, 'category/category_group.html', context)

def addproduct(request):
    form = ProductAdd()
    context = {'form': form}
    if request.method == 'POST':
        data = request.POST
        form = ProductAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category = data ['category']
            name = data ['name']
            slug = data ['slug']
            description = data ['description']
            price = data ['price']
            aval = data.get('available', False)
            available = bool (aval)
            print (available)
            product, created  = Product.objects.get_or_create(name=name,category=category,slug = slug, defaults = {'description': description, 'price' : price, 'available': available})
            if created == False:
                msg = sweetify.success(request, 'You did it', text='Duplicate product message', persistent='Hell yeah')
                return render (request, 'product/productform.html')
            if available == False:
                msg = sweetify.warning(request, 'Product Added', text="Product won't be displayed to customers", persistent='Hell yeah')
            else:
                sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
            return redirect ('product')
        return render (request, 'product/productform.html', {'form': form} )
    return render (request, 'product/productform.html', context)


def detail_product(request, id):
    context = {'product':Product.objects.filter(id=id), 'detail_prod': Product.objects.all()}
    if request.method=='POST':
        return render (request, 'product/cart.html')
    return render (request, 'product/detail.html', context)
