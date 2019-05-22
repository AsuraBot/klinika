from django.urls import path
from django.contrib.auth.decorators import login_required
from peoples import views

urlpatterns = [
    path('doctors/<doctors_id>/', views.doctors_detail, name='doctors_detail'),
    path('doctors/', views.doctors, name='doctors'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.MyUserCreationView.as_view(), name='register'),
    path('profile/', login_required(views.MyProfileView.as_view()), name='profile'),
]