from staticpages.models import About

def gettingabouts(request):
    abouts = About.objects.all()

    context = {
        'abouts': abouts,
    }

    return context