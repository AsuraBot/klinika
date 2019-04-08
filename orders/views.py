from django.shortcuts import render
from django.http import JsonResponse
from services.models import ServiceMain, Service
from peoples.models import Doctor
from schedules.models import WorkCity, WorkDate

# Create your views here.


def booknow(request):
    mainservices = ServiceMain.objects.all()
    doctors = Doctor.objects.all()

    context = {
        'mainservices' : mainservices,
        'doctors' : doctors,
    }

    return render(request, 'orders/booknow.html', context)


def doctorfilter(request):
    service_id = int(request.POST.get('service_id'))

    service = Service.objects.get(id=service_id)
    doctors = Doctor.objects.filter(services__in=[service])
    
    doctors_id = [doctor.id for doctor in doctors]
    doctors_name = [doctor.name for doctor in doctors]

    context = {
        'doctors_id' : doctors_id,
        'doctors_name' : doctors_name,
    }

    return JsonResponse(context)


def cityfilter(request):
    doctor_id = int(request.POST.get('doctor_id'))

    doctor = Doctor.objects.get(id=doctor_id)
    workdates = WorkDate.objects.filter(doctor__in=[doctor]).distinct()
    
    cities_name = [workdate.workcity.city for workdate in workdates]
    cities_id = [workdate.workcity.id for workdate in workdates]

    context = {
        'cities_name': cities_name,
        'cities_id': cities_id,
    }

    return JsonResponse(context)


def datetimefilter(request):
    doctor_id = int(request.POST.get('doctor_id'))
    city_id = int(request.POST.get('city_id'))

    doctor = Doctor.objects.get(id=doctor_id)
    city = WorkCity.objects.get(id=city_id)
    workdates = WorkDate.objects.filter(doctor=doctor, workcity=city)
    
    schedule = {}
    times =[]

    for workdate in workdates:
        for worktime in workdate.worktimes.all():
            times.append(worktime.time.strftime('%H:%M'))
        schedule[workdate.date.strftime('%d.%m.%Y')] = times
        times = []
   
    context = {
        'schedule': schedule,
    }

    return JsonResponse(context)