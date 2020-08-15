"""swan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import index, Administrator
from product.views import category_group, category_delete, category_update, update_product, delete_product, CategoryView, \
    ProductView, addproduct, category_add, add_product, StoreView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('administrator/', Administrator.as_view(), name = 'administrator'),
    # path('category/', category, name = 'category'),
    path ('category/', CategoryView.as_view(), name = 'category'),
    path ('store/', StoreView.as_view(), name = 'store'),
    # path('product/', product, name = 'product'),
    path('product/', ProductView.as_view(), name = 'product'),
    path('category_add/', category_add, name = 'category_add'),
    # path ('category_add/', CategoryAddView.as_view(), name = 'category_add'),
    path('category_update/<int:id>', category_update, name = 'update_category'),
    path('category_group/<int:id>', category_group, name = 'group_category'),
    path('category_delete/<int:id>', category_delete, name = 'delete_category'),
    path('add_product/', add_product, name = 'add_product'),
    # path('add_product/', ProductAddView.as_view(), name = 'add_product'),
    path('update_product/<int:id>', update_product, name = 'product_update'),
    path('delete_product/<int:id>', delete_product, name = 'product_delete'),
    path('form', addproduct, name = 'addproduct'),
]
