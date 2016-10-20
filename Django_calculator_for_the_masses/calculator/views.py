# from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView

from django.views.generic.edit import CreateView

from calculator.models import Calc, Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class CalcView(ListView):
    template_name = 'calcs.html'
    model = Calc


class ProfileDetailView(DetailView):
    model = Profile


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class CalcCreateView(CreateView):
    model = Calc
    success_url = "/"
    fields = ("num1", "num2", "operator", "description")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super().form_valid(form)

# def get_context_data(self):
#     context = super().get_context_data()
#     context["object_list"] = Special.objects.all()
#     return context
