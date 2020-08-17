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

# class CategoryView(View):
#     def get (self, request):
#         category = Category.objects.all()
#         context = {'category': category}
#         return render (request, 'category/category_display.html', context)

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

# class StoreView(ListView):
#     template_name = 'product/store.html'
#     model = Product
#     context_object_name = 'product'

def storeProduct (request):
    product = Product.objects.all()
    total = 0
    for i in product:
        total += product['category.name']
    return render(request, 'product/store.html', {'product': product, 'total': total})


    # def get (self, request):
    #     category = Category.objects.all()
    #     context = {'category': category}
    #     return render (request, 'category/category_display.html', context)


# class CategoryAddView(View):
#         def get (self, request):
#             category = Category.objects.all()
#             context = {'category': category}
#             return render (request, 'category/category_add.html', context)

#         def post (self, request):
#             data=request.POST
#             name = data ['name']
#             slug = data ['slug']
#             objt, created = Category.objects.get_or_create(name = name, defaults = {'slug' : slug} )
#             if created==False:
#                 msg = sweetify.success(request, 'You did it', text='Category already existed', persistent='Hell yeah')
#                 context = {'msg' :msg}
#                 return render (request, 'category/category_add.html', context )
#             sweetify.success(request, 'You did it', text='Category Successfully added', persistent='Hell yeah')        
#             return redirect ('category')

# def category(request):
#     # template = loader.get_template('category/category_display.html')
#     category = Category.objects.all()
#     context = {'category': category}
#     # return HttpResponse (template.render({'category': category}, request))
#     return render (request, 'category/category_display.html', context)

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


# def category_add(request):
#     # template = loader.get_template('category/category_add.html')
#     # category = Category.objects.all()
#     if request.method == 'POST':
#         data=request.POST
#         name = data ['name']
#         slug = data ['slug']
#         # chck = Category.objects.filter(slug=slug)
#         objt, created = Category.objects.get_or_create(name = name, defaults = {'slug' : slug} )
#         if created==False:
#             # obj_exists = True
#             # messages.warning(request, 'You are trying to enter duplicate name!!!')
#             msg = sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
#             context = {'msg' :msg}
#             # return HttpResponse (template.render(context, request))
#             return render (request, 'category/category_add.html', context )
#         # obj = Category.objects.create(name = name, slug = slug)
#         sweetify.success(request, 'You did it', text='Category Successfully added', persistent='Hell yeah')        
#         # return HttpResponseRedirect (reverse('category'))
#         return redirect ('category')    
#     # return HttpResponse (template.render({}, request))
#     return render (request, 'category/category_add.html')

class ProductView (ListView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'product'

    # def get(self, request):
    #     product = Product.objects.all()
    #     context = {'product': product}
    #     return render (request, 'product/product.html', context)

# class ProductView (View):
#     def get(self, request):
#         product = Product.objects.all()
#         context = {'product': product}
#         return render (request, 'product/product.html', context)

class ProductAddView (CreateView):
    template_name = 'product/add_product.html'
    # model = Product
    form_class = AddProductForm
    # fields = ['category','name', 'slug', 'description', 'price', 'available']
    success_url = reverse_lazy ('product')
    # context_object_name = 'add_product'

    # def get_context_data(self, **kwargs):
    #     kwargs.setdefault('view', self)
    #     if self.extra_context is not None:
    #         kwargs.update(self.extra_context)
    #     kwargs ['message'] = sweetify.success(self.request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
    #     kwargs ['product'] = Product.objects.create()
    #     return kwargs

# class ProductAddView (View):
#     def get(self, request):
#         context = {'categories':Category.objects.all()}
#         return render (request, 'product/add_product.html', context)
    
#     def post (self, request):
#         data = request.POST
#         category_id = data ['category']
#         name = data ['name']
#         slug = data ['slug']
#         # image = data ['image']
#         description = data ['description']
#         price = data ['price']
#         aval = data.get('available', False)
#         available = bool (aval)
#         print (available)
#         product, created  = Product.objects.get_or_create(name=name,category_id=category_id,slug = slug, defaults = {'description': description, 'price' : price, 'available': available})
#         if created == False:
#             msg = sweetify.success(request, 'You did it', text='Duplicate product message', persistent='Hell yeah')
#             # return HttpResponse (template.render({}, request))
#             return render (request, 'product/add_product.html')
#         if available == False:
#             msg = sweetify.warning(request, 'Product Added', text="Product won't be displayed to customers", persistent='Hell yeah')
#         else:
#             sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
#         # return HttpResponseRedirect (reverse('product'))
#         return redirect ('product')


# def product(request):
#     # template = loader.get_template('product/product.html')
#     product = Product.objects.all()
#     context = {'product': product}
#     # return HttpResponse (template.render({'product': product}, request))
#     return render (request, 'product/product.html', context)

def add_product(request):
    form = AddProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            image = Product.objects.filter(image)
            

            form.save()
            sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
            return redirect ('product')
        context = {'form': form}
        return render (request, 'product/add_product.html', context)
    return render (request, 'product/add_product.html', context)

# def add_product(request):
#     # template = loader.get_template('product/add_product.html')
#     if request.method == "POST":
#         data = request.POST
#         category_id = data ['category']
#         name = data ['name']
#         slug = data ['slug']
#         # image = data ['image']
#         description = data ['description']
#         price = data ['price']
#         aval = data.get('available', False)
#         available = bool (aval)
#         print (available)
#         product, created  = Product.objects.get_or_create(name=name,category_id=category_id,slug = slug, defaults = {'description': description, 'price' : price, 'available': available})
#         if created == False:
#             msg = sweetify.success(request, 'You did it', text='Duplicate product message', persistent='Hell yeah')
#             # return HttpResponse (template.render({}, request))
#             return render (request, 'product/add_product.html')
#         if available == False:
#             msg = sweetify.warning(request, 'Product Added', text="Product won't be displayed to customers", persistent='Hell yeah')
#         else:
#             sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
#         # return HttpResponseRedirect (reverse('product'))
#         return redirect ('product')
#     context = {
#         'categories':Category.objects.all()
#     }
#     # return HttpResponse (template.render(context, request))
#     return render (request, 'product/add_product.html', context)
def update_product(request, id):
    # template = loader.get_template('product/add_product.html')
    # product = Product.objects.get(id=id)
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

# def update_product(request, id):
#     # template = loader.get_template('product/add_product.html')
#     # product = Product.objects.get(id=id)
#     product = get_object_or_404(Product, id=id)
#     categories = Category.objects.all()
#     if request.method == "POST":
#         data = request.POST
#         print (data)
#         product.category_id = data ['category']
#         product.name = data ['name']
#         product.slug = data ['slug']
#         # image = data ['image']
#         product.description = data ['description']
#         product.price = data ['price']
#         product.aval = data.get('available', False)
#         product.available = bool (product.aval)
#         product.save()
#         sweetify.success(request, 'You did it', text='Product Successfully Updated', persistent='Hell yeah')        
#         # return HttpResponseRedirect (reverse('product'))
#         return redirect ('product')
#     context = {'product': product, 'update': True, 'categories': categories}
#     # return HttpResponse (template.render(context, request))
#     return render (request, 'product/add_product.html', context)

def delete_product (request, id):
    # template = loader.get_template('product/product.html')
    # product = Product.objects.get(id=id)
    product = get_object_or_404 (Product, id=id)
    product.delete()
    sweetify.success(request, 'You did it', text='Product deleted successfully', persistent='Hell yeah')        
    # return HttpResponseRedirect (reverse('product'))
    return redirect ('product')

def category_update(request, id):
    # template = loader.get_template('category/category_add.html')
    category = Category.objects.get(id=id)
    # print (category.id)
    if request.method == 'POST':
        data = request.POST
        category.name = data ['name']
        category.slug = data ['slug']
        category.save()
        sweetify.success(request, 'You did it', text='Updated Successfully', persistent='Hell yeah')        
        # return HttpResponseRedirect (reverse('category'))
        return redirect ('category')
    context = {'category': category, 'update': True}
    # return HttpResponse (template.render({'category': category, 'update': True}, request))
    return render (request, 'category/category_add.html', context)



def category_delete(request, id):
    # template = loader.get_template('category/category_display.html')
    # category = Category.objects.get(id=id)
    category = get_object_or_404(Category, id=id)
    category.delete()
    sweetify.success(request, 'You did it', text='Category deleted successfully', persistent='Hell yeah')        
    # return HttpResponseRedirect (reverse('category'))
    return redirect ('category')


def category_group(request, id):
    # template = loader.get_template('category/category_group.html')
    # group = Category.objects.get(id=id)
    group = get_object_or_404 (Category, id=id)
    context = group.products.all()
    try:
        title = group.products.all()[id].category
    except:
        title = 'No products available'
    context = {'group':context, 'title': title}
    # return HttpResponse (template.render({'group':context, 'title': title}, request))
    return render (request, 'category/category_group.html', context)

def addproduct(request):
    form = ProductAdd()
    context = {'form': form}
    if request.method == 'POST':
        data = request.POST
        # print (data) # prints in QueryDict Format
        form = ProductAdd(request.POST)
        # print (form.is_valid()) # check if the data is valid
        # print (form.errors) # print if errors in form
        if form.is_valid():
            data = form.cleaned_data
            # print (data) # prints in Dictionary Format
            category = data ['category']
            # print (type(category))
            name = data ['name']
            slug = data ['slug']
            # image = data ['image']
            description = data ['description']
            price = data ['price']
            aval = data.get('available', False)
            available = bool (aval)
            print (available)
            product, created  = Product.objects.get_or_create(name=name,category=category,slug = slug, defaults = {'description': description, 'price' : price, 'available': available})
            if created == False:
                msg = sweetify.success(request, 'You did it', text='Duplicate product message', persistent='Hell yeah')
                # return HttpResponse (template.render({}, request))
                return render (request, 'product/productform.html')
            if available == False:
                msg = sweetify.warning(request, 'Product Added', text="Product won't be displayed to customers", persistent='Hell yeah')
            else:
                sweetify.success(request, 'You did it', text='Product Successfully added', persistent='Hell yeah')        
            # return HttpResponseRedirect (reverse('product'))
            return redirect ('product')
        return render (request, 'product/productform.html', {'form': form} )
    return render (request, 'product/productform.html', context)
