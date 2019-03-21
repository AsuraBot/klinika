from django.shortcuts import render
from services.models import ServiceMain

# Create your views here.

def services(request):
    context = {
    }
    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    service = ServiceMain.objects.get(id=int(about_id))

    context = {
        'service': service,
    }
    return render(request, 'services/servicedetail.html', context)