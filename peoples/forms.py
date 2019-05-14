from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Логин', 'class': 'form-control', 'id': 'inputlogin'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputpassword'}))