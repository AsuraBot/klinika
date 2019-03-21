from django.shortcuts import render
from staticpages.models import About

# Create your views here.

def about(request):
    abouts = About.objects.all()

    context = {
        'abouts': abouts,
    }
    return render(request, 'staticpages/abouts.html', context)


def about_detail(request, about_id):
    aboutdetails = About.objects.get(id=int(about_id))

    context = {
        'aboutdetails': aboutdetails,
    }
    return render(request, 'staticpages/aboutdetails.html', context)