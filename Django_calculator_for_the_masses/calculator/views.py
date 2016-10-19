# from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from calculator.models import Calc


# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    model = Calc


class ProfileView(TemplateView):
    template_name = 'profile.html'
