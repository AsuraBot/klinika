from staticpages.models import About
from cities.models import UserCity

def gettingabouts(request):
    abouts = About.objects.all()
    cities = UserCity.objects.all()

    context = {
        'abouts': abouts,
        'cities': cities,
    }

    return context