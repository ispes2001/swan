from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
   
class Administrator (TemplateView):
    template_name = 'base_admin.html'
