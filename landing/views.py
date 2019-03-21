from django.shortcuts import render
from services.models import Service

# Create your views here.

def index(request):
    allservices = Service.objects.filter(is_active=True)

    context = {
        'allservices': allservices,
    }
    return render(request, 'landing/index.html',context)