from django.shortcuts import render
from services.forms import ServiceForm
from peoples.forms import DoctorForm
from schedules.forms import CityForm

# Create your views here.

def booknow(request):
    service_form = ServiceForm()
    doctor_form = DoctorForm()
    city_form = CityForm()

    context = {
        'service_form': service_form,
        'doctor_form': doctor_form,
        'city_form': city_form,
    }

    return render(request, 'orders/booknow.html', context)