# from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from django.views.generic.edit import CreateView

from calculator.models import Calc

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class CalcView(ListView):
    template_name = "index.html"
    model = Calc


class ProfileView(TemplateView):
    template_name = 'profile.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class CalcCreateView(CreateView):
    model = Calc
    success_url = "/"
    fields = ("num1", "")
