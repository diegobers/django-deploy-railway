from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView


class LoginAuthView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'



