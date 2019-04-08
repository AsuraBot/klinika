from django.urls import path
from orders import views

urlpatterns = [
    path('booknow/', views.booknow, name='booknow'),
    path('doctorfilter/', views.doctorfilter, name='doctorfilter'),
    path('cityfilter/', views.cityfilter, name='cityfilter'),
    path('datetimefilter/', views.datetimefilter, name='datetimefilter'),
]