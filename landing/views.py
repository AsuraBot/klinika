from django.shortcuts import render, render_to_response
from django.template import RequestContext
from services.models import ServiceMain
from news.models import Novost

# Create your views here.

def index(request):
    popular_services = ServiceMain.objects.all()[:4]
    last_news = Novost.objects.filter(is_active=True)[:4]

    context = {
        'popular_services': popular_services,
        'last_news': last_news,
    }
    return render(request, 'landing/index.html',context)

 
def e_handler404(request):
    response = render(request, 'errorpages/404.html', {})
    response.status_code = 404
    return response
 
 
def e_handler500(request):
    response = render(request, 'errorpages/500.html', {})
    response.status_code = 500
    return response