from django.urls import path
from peoples import views

urlpatterns = [
    path('doctors/<doctors_id>/', views.doctors_detail, name='doctors_detail'),
    path('doctors/', views.doctors, name='doctors'),
    path('login/', views.MyLoginView.as_view(), name='login'),
]