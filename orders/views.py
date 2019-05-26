from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from services.models import ServiceMain, Service
from users.models import UserProfile, MyGroup
from schedules.models import WorkCity, WorkDate
from orders.models import ServiceInOrder, AnalysisInOrder, Order

# Create your views here.


def booknow(request):
    mainservices = ServiceMain.objects.all()
    
    service_id = request.GET.get('service_id', '-1')

    context = {
        'mainservices' : mainservices,
        'service_id' : int(service_id),
    }

    return render(request, 'orders/booknow.html', context)


def doctorbooknow(request):
    groups = MyGroup.objects.filter(name__icontains='Врач')
    doctors = UserProfile.objects.filter(groups__in=groups)

    doctor_id = request.GET.get('doctor_id', '-1')

    context = {
        'doctors' : doctors,
        'doctor_id' : int(doctor_id),
    }

    return render(request, 'orders/doctorbooknow.html', context)


def doctorfilter(request):
    service_id = int(request.POST.get('service_id'))

    service = Service.objects.get(id=service_id)
    groups = MyGroup.objects.filter(name__icontains='Врач')
    doctors = UserProfile.objects.filter(groups__in=groups).filter(services__in=[service])

    workdates = []

    for doctor in doctors:
        for workdate in doctor.workdates.all():
            workdates.append(workdate)
    
    doctors = []

    for workdate in workdates:
        if workdate.date > datetime.now().date():
            for worktime in workdate.worktimes.all():
                doctors.append(workdate.doctor)

        if workdate.date == datetime.now().date():
            for worktime in workdate.worktimes.all():
                if worktime.time >= datetime.now().time():
                    doctors.append(workdate.doctor)

    doctors = set(doctors)

    doctors_id = [doctor.id for doctor in doctors]
    doctors_name = [doctor.last_name + ' ' + doctor.first_name + ' ' + doctor.sur_name for doctor in doctors]

    context = {
        'doctors_id' : doctors_id,
        'doctors_name' : doctors_name,
        'service_price' : service.price,
    }

    return JsonResponse(context)


def cityfilter(request):
    doctor_id = int(request.POST.get('doctor_id'))

    doctor = UserProfile.objects.get(id=doctor_id)
    doctorwork = WorkDate.objects.filter(doctor__in=[doctor])

    cities_name = []
    cities_id = []

    for workdate in doctorwork:
        if workdate.date > datetime.now().date():
            if workdate.workcity.city not in cities_name:
                cities_name.append(workdate.workcity.city)
            if workdate.workcity.id not in cities_id:
                cities_id.append(workdate.workcity.id)

        if workdate.date == datetime.now().date():
            for worktime in workdate.worktimes.all():
                if worktime.time >= datetime.now().time():
                    if workdate.workcity.city not in cities_name:
                        cities_name.append(workdate.workcity.city)
                    if workdate.workcity.id not in cities_id:
                        cities_id.append(workdate.workcity.id)

    context = {
        'cities_name': cities_name,
        'cities_id': cities_id,
    }

    return JsonResponse(context)


def datetimefilter(request):
    doctor_id = int(request.POST.get('doctor_id'))
    city_id = int(request.POST.get('city_id'))

    doctor = UserProfile.objects.get(id=doctor_id)
    city = WorkCity.objects.get(id=city_id)
    workdates = WorkDate.objects.filter(doctor=doctor, workcity=city)
    
    schedule = {}
    times =[]

    for workdate in workdates:
        if workdate.date > datetime.now().date():
            for worktime in workdate.worktimes.all():
                times.append(worktime.time.strftime('%H:%M'))

        if workdate.date == datetime.now().date():
            for worktime in workdate.worktimes.all():
                if worktime.time >= datetime.now().time():
                    times.append(worktime.time.strftime('%H:%M'))

        if len(times) > 0:
            schedule[workdate.date.strftime('%d.%m.%Y')] = times
            times = []

    context = {
        'schedule': schedule,
    }

    return JsonResponse(context)


def ordercreate(request):
    service_id = int(request.POST.get('service_id'))
    doctor_id = int(request.POST.get('doctor_id'))
    city_id = int(request.POST.get('city_id'))
    date = datetime.strptime(request.POST.get('date'), '%d.%m.%Y')
    time = request.POST.get('time')
    client_name = request.POST.get('client_name')
    client_address = request.POST.get('client_address')
    client_phone = request.POST.get('client_phone')
    client_dob = request.POST.get('client_dob')
    client_mail = request.POST.get('client_mail')

    service = Service.objects.get(id=service_id)
    doctor = UserProfile.objects.get(id=doctor_id)
    city = WorkCity.objects.get(id=city_id)

    total_price = service.price

    order = Order.objects.create(
        client_name = client_name,
        client_address = client_address,
        client_phone =  client_phone,
        client_dob = client_dob,
        client_mail = client_mail,
        total_price = total_price,
    )

    serviceinorder = ServiceInOrder.objects.create(
        order = order,
        service = service,
        doctor = doctor,
        city = city.city,
        date = date,
        time = time,
        price = service.price,
    )

    context = {
        'ordercity': serviceinorder.city,
    }

    return JsonResponse(context) 

def servicefilter(request):
    doctor_id = request.POST.get('doctor_id')

    doctor = UserProfile.objects.get(id=int(doctor_id))
    services = Service.objects.filter(doctors__in=[doctor], is_active=True)

    services_id = [service.id for service in services]
    services_name = [service.name for service in services]

    context = {
        'services_id' : services_id,
        'services_name' : services_name,
    }

    return JsonResponse(context)