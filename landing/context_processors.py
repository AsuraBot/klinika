from staticpages.models import About
from services.models import ServiceMain

def gettingabouts(request):
    abouts = About.objects.all()
    servicemains = ServiceMain.objects.filter(is_active=True)

    context = {
        'abouts': abouts,
        'servicemains': servicemains,
    }

    return context