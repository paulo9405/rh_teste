
from django.contrib import admin
from django.urls import path, include
from core.views import create_company
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls')),
    path('', include('core.urls')),
    path('logo', create_company, name='logo'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
