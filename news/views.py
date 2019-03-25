from django.shortcuts import render
from news.models import Novost

# Create your views here.

def news(request):
    news = Novost.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'news/news.html', context)