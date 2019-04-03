from dal import autocomplete
from django import forms
from schedules.models import WorkCity


class CityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['citychoice'] = forms.ModelChoiceField(
            queryset=WorkCity.objects.all(),
            widget=autocomplete.ModelSelect2(url='city-autocomplete', attrs={'class': 'form-control'}),
        )