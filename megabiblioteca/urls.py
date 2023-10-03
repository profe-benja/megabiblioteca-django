from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('biblioteca.urls')),
    path('api/v1/', include('rest_api.urls')),
]
