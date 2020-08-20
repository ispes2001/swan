from django.urls import path
from django.conf.urls.static import static
from home.views import index

urlpatterns = [
    path('', index, name = 'home'),
]
