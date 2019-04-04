from django.shortcuts import render
from django.http import JsonResponse
from orders.forms import ServiceForm
from services.models import ServiceMain, Service
from peoples.models import Doctor

# Create your views here.

def booknow(request):
    form = ServiceForm()
    mainservices = ServiceMain.objects.all()
    doctors = Doctor.objects.all()

    context = {
        'form': form,
        'mainservices' : mainservices,
        'doctors' : doctors,
    }

    return render(request, 'orders/booknow.html', context)

def example(request):
    service_id = int(request.POST.get('service_id'))

    service = Service.objects.get(id=service_id)
    doctors = Doctor.objects.filter(services__in=[service])

    context = {
    }

    return JsonResponse(context)