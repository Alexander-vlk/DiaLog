from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome_app.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
