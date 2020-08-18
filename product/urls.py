from django.urls import path
from product.views import category_group, category_delete, category_update, update_product, delete_product, CategoryView, \
    ProductView, addproduct, category_add, add_product, storeProduct, ProductAddView
from django.conf.urls.static import static

urlpatterns = [
    path ('category/', CategoryView.as_view(), name = 'category'),
    path ('store/', storeProduct.as_view(), name = 'store'),
    path('product/', ProductView.as_view(), name = 'product'),
    path('category_add/', category_add, name = 'category_add'),
    path('category_update/<int:id>', category_update, name = 'update_category'),
    path('category_group/<int:id>', category_group, name = 'group_category'),
    path('category_delete/<int:id>', category_delete, name = 'delete_category'),
    path('add_product/', ProductAddView.as_view(), name = 'add_product'),
    path('update_product/<int:id>', update_product, name = 'product_update'),
    path('delete_product/<int:id>', delete_product, name = 'product_delete'),
    path('form', addproduct, name = 'addproduct'),
]