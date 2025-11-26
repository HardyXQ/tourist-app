from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import index, map_view, location_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('map/', map_view, name='map'),
    path('location/<int:location_id>/', location_detail, name='location_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)