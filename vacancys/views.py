from django.shortcuts import render
from vacancys.models import Vacancy

# Create your views here.

def vacancys(request):
    allvacancys = Vacancy.objects.all()

    context = {
        'allvacancys': allvacancys,
    }
    return render(request, 'vacancys/vacancys.html', context)