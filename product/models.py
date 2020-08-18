from django.db import models
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url (self):
        return reverse_lazy ('update_category', args=[self.id])
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # fs = FileSystemStorage()
    image = models.ImageField(upload_to="image")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

        
    def get_absolute_url (self):
        return reverse_lazy ('product_update', args = [self.id])

# class ProductImage (models.Model):
#     fs = FileSystemStorage()
#     caption = models.CharField(max_length=200)
#     image = models.ImageField(storage=fs, upload_to="image")

