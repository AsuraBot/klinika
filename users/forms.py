from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин', 'class': 'form-control', 'id': 'inputlogin'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputpassword'}))


class MyUserCreationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин', 'class': 'form-control', 'id': 'inputlogin'}))
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'form-control'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")