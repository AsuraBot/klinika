from django.urls import path
from peoples import views

urlpatterns = [
    path('<doctors_id>/', views.doctors_detail, name='doctors_detail'),
    path('', views.doctors, name='doctors'),
]