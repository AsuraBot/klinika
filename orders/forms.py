from dal import autocomplete
from django import forms
from services.models import Service
from peoples.models import Doctor
from schedules.models import WorkCity


class ServiceForm(forms.Form):
    servicechoice = forms.ModelChoiceField(
    queryset=Service.objects.filter(is_active=True),
    widget=autocomplete.ModelSelect2(url='service-autocomplete', attrs={'class': 'form-control'}),
    )

    doctorchoice = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(),
        widget=autocomplete.ModelSelect2(url='doctor-autocomplete', attrs={'class': 'form-control'}),
    )

    citychoice = forms.ModelChoiceField(
        queryset=WorkCity.objects.filter(),
        widget=autocomplete.ModelSelect2(url='city-autocomplete', attrs={'class': 'form-control'}),
    )