from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from landing.views import e_handler404, e_handler500


admin.site.site_header = 'Клиника'


handler404 = e_handler404
handler500 = e_handler500


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('imagefit/', include('imagefit.urls')),
    path('', include('landing.urls')),
    path('vacancys/', include('vacancys.urls')),
    path('other/', include('staticpages.urls')),
    path('services/', include('services.urls')),
    path('accounts/', include('users.urls')),
    path('news/', include('news.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)