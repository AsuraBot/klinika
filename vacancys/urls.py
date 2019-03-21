from django.urls import path
from vacancys import views


urlpatterns = [
    path('', views.vacancys, name='vacancys'),
]