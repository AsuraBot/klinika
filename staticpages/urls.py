from django.urls import path
from staticpages import views

urlpatterns = [
    path('<about_id>/', views.about_detail, name='about_detail'),
    path('', views.about, name='about'),
]