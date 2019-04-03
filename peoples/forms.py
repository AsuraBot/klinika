from dal import autocomplete
from django import forms
from peoples.models import Doctor


class DoctorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['doctorchoice'] = forms.ModelChoiceField(
            queryset=Doctor.objects.all(),
            widget=autocomplete.ModelSelect2(url='doctor-autocomplete', attrs={'class': 'form-control'}),
        )