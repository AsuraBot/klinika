from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from dal import autocomplete
from peoples.models import Doctor, DoctorMain
from peoples.forms import MyAuthenticationForm, MyUserCreationForm

# Create your views here.

def doctors(request):
    doctormains = DoctorMain.objects.all()

    context = {
        'doctormains': doctormains,
    }
    return render(request, 'doctors/doctors.html', context)


def doctors_detail(request, doctors_id):
    doctor = Doctor.objects.get(id=int(doctors_id))

    context = {
        'doctor': doctor,
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
        context = {

        }
        return render(request, 'peoples/profile.html', context)

    # def post(self, request):