from django import forms
from django.forms import ModelForm

from .models import *

class ProductAdd(forms.Form):
    category = forms.ModelChoiceField(Category.objects.all(), empty_label="Choose a Category")
    name = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=200)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,null=True)
    description = forms.CharField(required=False)
    price = forms.DecimalField()
    available = forms.BooleanField(required=True)

class AddProductForm(forms.ModelForm):    
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {'description': forms.Textarea(attrs={'rows':2})}

class AddCategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = '__all__'
