from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from dal import autocomplete
from users.models import UserProfile, DoctorMain, MyGroup
from users.forms import MyAuthenticationForm, MyUserCreationForm
from schedules.models import WorkDate
from cities.models import UserCity

# Create your views here.

def doctors(request):
    doctormains = DoctorMain.objects.all()

    context = {
        'doctormains': doctormains,
    }
    return render(request, 'doctors/doctors.html', context)


def doctors_detail(request, doctors_id):
    doctor = get_object_or_404(UserProfile, id=int(doctors_id))
    workdates = WorkDate.objects.filter(doctor=doctor)
    cities = UserCity.objects.filter(workdates__in=workdates).distinct()

    context = {
        'doctor': doctor,
        'workdates': workdates,
        'cities': cities,
    }
    return render(request, 'doctors/doctorsdetail.html', context)


class MyLoginView(LoginView):
    template_name = 'peoples/login.html'
    form_class = MyAuthenticationForm


class MyUserCreationView(View):
    
    def get(self, request):
        form = MyUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'peoples/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.username = form.cleaned_data.get('username')
            newuser.set_password(form.cleaned_data.get('password1'))
            newuser.save()

            return redirect('profile')
        else:
            context = {
                'form': form,
            }
            return render(request, 'peoples/register.html', context)


class MyProfileView(View):

    def get(self, request):
        user = request.user

        if user.groups.filter(name='Клиент').exists():
            context = {

            }
            return render(request, 'peoples/client_profile.html', context)

        if user.groups.filter(name='Оператор').exists():
            context = {

            }
            return render(request, 'peoples/operator_profile.html', context)

        if user.groups.filter(name='Старший оператор').exists():    
            context = {

            }
            return render(request, 'peoples/mainoperator_profile.html', context)

        if user.groups.filter(name='Агент').exists():
            context = {

            }
            return render(request, 'peoples/agent_profile.html', context)

        if user.groups.filter(name='Внешний доктор').exists():
            context = {

            }
            return render(request, 'peoples/outside_doctor_profile.html', context)

        if user.groups.filter(name='Врач').exists():    
            context = {

            }
            return render(request, 'peoples/doctor_profile.html', context)

        if user.groups.filter(name='Директор').exists():    
            context = {

            }
            return render(request, 'peoples/director_profile.html', context)

    # def post(self, request):