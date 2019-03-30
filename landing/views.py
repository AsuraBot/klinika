from django.shortcuts import render
from services.models import ServiceMain
from news.models import Novost

# Create your views here.

def index(request):
    popular_services = ServiceMain.objects.filter(is_active=True)[:4]
    last_news = Novost.objects.filter(is_active=True)[:4]

    context = {
        'popular_services': popular_services,
        'last_news': last_news,
    }
    return render(request, 'landing/index.html',context)