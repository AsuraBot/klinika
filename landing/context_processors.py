from staticpages.models import About
from schedules.models import WorkCity

def gettingabouts(request):
    abouts = About.objects.all()
    cities = WorkCity.objects.all()

    context = {
        'abouts': abouts,
        'cities': cities,
    }

    return context