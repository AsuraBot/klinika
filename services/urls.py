from django.urls import path
from services import views


urlpatterns = [
    path('<service_id>/', views.service_detail, name='service_detail'),
    path('', views.services, name='services'),
]