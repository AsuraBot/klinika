from dal import autocomplete
from django import forms
from services.models import Service


class ServiceForm(forms.Form):
    # name = forms.ModelChoiceField(
    #     queryset=Service.objects.filter(is_active=True) ,
    #     widget=autocomplete.ModelSelect2(url='service-autocomplete')
    # )

    # class Meta:
    #     model = Service
    #     fields = ['name']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['servicechoice'] = forms.ModelChoiceField(
            queryset=Service.objects.filter(is_active=True),
            widget=autocomplete.ModelSelect2(url='service-autocomplete', attrs={'class': 'form-control'}),
        )