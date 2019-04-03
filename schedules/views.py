from django.shortcuts import render
from dal import autocomplete
from schedules.models import WorkCity

# Create your views here.

class CityAutocomplete(autocomplete.Select2QuerySetView):
     def get_queryset(self):
        qs = City.objects.all() 
        if self.q:
            qs = qs.filter(name__icontains=self.q) 
        return qs