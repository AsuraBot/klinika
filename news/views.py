from django.shortcuts import render
from news.models import Novost

# Create your views here.

def news(request):
    news = Novost.objects.filter(is_active=True)

    context = {
        'news': news,
    }
    return render(request, 'news/news.html', context)

def news_detail(request, news_id):
    news = Novost.objects.get(id=int(news_id))

    context = {
        'news': news,
    }
    return render(request, 'news/newsdetail.html', context)