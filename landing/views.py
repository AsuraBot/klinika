from django.shortcuts import render, render_to_response
from django.template import RequestContext
from services.models import Service
from news.models import Novost
from users.models import UserProfile, MyGroup

# Create your views here.

def index(request):
    popular_services = Service.objects.all().order_by('-counter')[:6]
    last_news = Novost.objects.filter(is_active=True)[:4]
    groups = MyGroup.objects.filter(name__icontains='Врач')
    index_doctors  = UserProfile.objects.filter(groups__in=groups)[:5]

    context = {
        'popular_services': popular_services,
        'last_news': last_news,
        'index_doctors': index_doctors,
    }
    return render(request, 'index.html',context)

 
def e_handler404(request):
    response = render(request, 'errorpages/404.html', {})
    response.status_code = 404
    return response
 
 
def e_handler500(request):
    response = render(request, 'errorpages/500.html', {})
    response.status_code = 500
    return response