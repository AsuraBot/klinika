from django.urls import path
from orders import views
from services.views import ServiceAutocomplete
from peoples.views import DoctorAutocomplete
from schedules.views import CityAutocomplete

urlpatterns = [
    path('booknow/', views.booknow, name='booknow'),
    path('service-autocomplete/', ServiceAutocomplete.as_view(), name='service-autocomplete'),
    path('doctor-autocomplete/', DoctorAutocomplete.as_view(), name='doctor-autocomplete'),
    path('city-autocomplete/', CityAutocomplete.as_view(), name='city-autocomplete'),
    path('example/', views.example, name='example')
]