from django.urls import path
from account.views import Administrator
from django.conf.urls.static import static

urlpatterns = [
    path('administrator/', Administrator.as_view(), name = 'administrator'),
]
