from django.contrib import admin
from django.urls import path, include
from account.views import index, Administrator
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

