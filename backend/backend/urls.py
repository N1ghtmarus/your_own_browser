from django.contrib import admin
from django.urls import path
from django.urls import include

from .yasg import urlpatterns as docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += docs_urls
