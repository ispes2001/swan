from django.urls import path
from account.views import index, Administrator
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'home'),
    path('administrator/', Administrator.as_view(), name = 'administrator'),
]
