from django.shortcuts import render
from reviews.models import Review

# Create your views here.

def reviews(request):
    allreview = Review.objects.all()

    context = {
        'allreview': allreview,
    }
    return render(request, 'reviews/review.html', context)