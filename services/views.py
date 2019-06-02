from django.shortcuts import render, get_object_or_404
from dal import autocomplete
from services.models import Service, ServiceMain

# Create your views here.

def services(request):
    servicemains = ServiceMain.objects.all()

    context = {
        'servicemains': servicemains,
    }
    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=int(service_id))

    context = {
        'service': service,
    }
    return render(request, 'services/servicedetail.html', context)