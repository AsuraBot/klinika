from django.shortcuts import render

# Create your views here.

def booknow(request):

    context = {
    }

    return render(request, 'orders/booknow.html', context)