<<<<<<< HEAD
# from django.db import models
# from swan.choice import *

# # Create your models here.
# class Profile (models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email =  models.EmailField(max_length=200)
#     phone = models.CharField(max_length=12)
#     dob = models.DateField(auto_now=False, auto_now_add=False)
#     address = models.CharField(max_length=200)
#     order = models.OneToOneField('Order', on_delete=models.CASCADE)

# # class Address (models.Model):
# #     # country = ChoiceField
# #     # state = ChoiceField
# #     # district = ChoiceField
# #     street = models.CharField(max_length=30)

# class User (models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     # social authentication


# class Category (models.Model):
#     cat_name = models.CharField(max_length=30)
#     products = models.ManyToManyField('Product')

# class Product (models.Model):
#     product_name = models.CharField(max_length=50)
#     highlight = models.CharField(max_length=100)
#     description = models.TextField(max_length=300)
#     price = models.FloatField()

# class Delivery (models.Model):
#     weight = models.FloatField()
#     dimenstions = models.FloatField()
#     delivery_type = models.CharField (max_length=30, choices=DELIVERY_CHOICES)
#     cost = models.FloatField()

# class Stock (models.Model):
#     availability = models.BooleanField()
#     quantity = models.IntegerField()
#     product = models.OneToOneField(Product, on_delete=models.CASCADE)

# class Service (models.Model):
#     warranty_type = models.CharField (max_length=50, choices=WARRANTY_CHOICES)
#     warranty_period = models.IntegerField()
#     policy = models.TextField(max_length=300)

# class Order (models.Model):
#     order_date = models.DateField(auto_now_add=True)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     delivery = models.OneToOneField('Delivery', on_delete=models.CASCADE)
#     order_status = models.CharField (max_length=50, choices=ORDER_STATUS_CHOICES)

# class Review (models.Model):
#     description = models.TextField(max_length=200)
#     star = models.CharField (max_length=50, choices=STAR_CHOICES)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)

# class Cart (models.Model):
#     numberofitem = models.IntegerField()
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     subtotal = models.FloatField()
#     delivery = models.OneToOneField('Delivery', on_delete=models.CASCADE)
#     total_cost = models.FloatField()
=======
from django.db import models
from swan.choice import *

# Create your models here.
class Profile (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email =  models.EmailField(max_length=200)
    phone = models.CharField(max_length=12)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=200)
    order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='profile')

# class Address (models.Model):
#     # country = ChoiceField
#     # state = ChoiceField
#     # district = ChoiceField
#     street = models.CharField(max_length=30)

class User (models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user')
    # social authentication


class Category (models.Model):
    cat_name = models.CharField(max_length=30)
    products = models.ManyToManyField('Product')

class Product (models.Model):
    product_name = models.CharField(max_length=50)
    highlight = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()

class Delivery (models.Model):
    weight = models.FloatField()
    dimenstions = models.FloatField()
    delivery_type = models.CharField (max_length=30, choices=DELIVERY_CHOICES)
    cost = models.FloatField()

class Stock (models.Model):
    availability = models.BooleanField()
    quantity = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stocks')

class Service (models.Model):
    warranty_type = models.CharField (max_length=50, choices=WARRANTY_CHOICES)
    warranty_period = models.IntegerField()
    policy = models.TextField(max_length=300)

class Order (models.Model):
    order_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    delivery = models.OneToOneField('Delivery', on_delete=models.CASCADE, related_name='order')
    order_status = models.CharField (max_length=50, choices=ORDER_STATUS_CHOICES)

class Review (models.Model):
    description = models.TextField(max_length=200)
    star = models.CharField (max_length=50, choices=STAR_CHOICES)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')

class Cart (models.Model):
    numberofitem = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='carts')
    subtotal = models.FloatField()
    delivery = models.OneToOneField('Delivery', on_delete=models.CASCADE, related_name='cart')
    total_cost = models.FloatField()
>>>>>>> 4528ed0c116921cdb842554740901019e89be5b9




