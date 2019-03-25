from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Клиника'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('landing.urls')),
    path('vacancys/', include('vacancys.urls')),
    path('other/', include('staticpages.urls')),
    path('services/', include('services.urls')),
    path('doctors/', include('peoples.urls')),
    path('news/', include('news.urls')),
    ]