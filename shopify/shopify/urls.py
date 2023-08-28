from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, docoment_root=settings.STATIC_ROOT)