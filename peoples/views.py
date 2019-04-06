from django.shortcuts import render
from dal import autocomplete
from peoples.models import Doctor, DoctorMain

# Create your views here.

def doctors(request):
    doctormains = DoctorMain.objects.all()

    context = {
        'doctormains': doctormains,
    }
    return render(request, 'doctors/doctors.html', context)


def doctors_detail(request, doctors_id):
    doctor = Doctor.objects.get(id=int(doctors_id))

    context = {
        'doctor': doctor,
    }
    return render(request, 'doctors/doctorsdetail.html', context)

def login(request):
    context = {

    }

    return render(request, 'login/login.html')