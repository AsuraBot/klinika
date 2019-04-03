from django.shortcuts import render
from dal import autocomplete
from services.models import Service, ServiceMain

# Create your views here.

def services(request):
    servicemains = ServiceMain.objects.filter(is_active=True)

    context = {
        'servicemains': servicemains,
    }
    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    service = Service.objects.get(id=int(service_id))

    context = {
        'service': service,
    }
    return render(request, 'services/servicedetail.html', context)


class ServiceAutocomplete(autocomplete.Select2QuerySetView):
     def get_queryset(self):
        qs = Service.objects.filter(is_active=True) 
        if self.q:
            qs = qs.filter(name__icontains=self.q) 
        return qs