from django.contrib import admin
from account import models

myModels = [models.Profile, models.User, models.Category, models.Product, models.Delivery, models.Stock, models.Service, models.Order, models.Review, models.Cart ]

admin.site.register(myModels)
