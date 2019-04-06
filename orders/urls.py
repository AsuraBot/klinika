from django.urls import path
from orders import views

urlpatterns = [
    path('booknow/', views.booknow, name='booknow'),
    path('example/', views.example, name='example'),
]