# from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView

from django.views.generic.edit import CreateView, UpdateView

from calculator.models import Operation, Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class OperationView(ListView):
    template_name = 'operations.html'
    model = Operation


class ProfileDetailView(DetailView):
    model = Profile


class ProfileUpdateView(UpdateView):
    template_name = 'profile.html'
    fields = ("access_level",)
    success_url = "/"  # reverse_lazy('profile_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class OperationCreateView(CreateView):
    model = Operation
    success_url = "/"
    fields = ("num1", "operator", "num2")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        instance.result = Operation.do_the_math
        return super().form_valid(form)

# def get_context_data(self):
#     context = super().get_context_data()
#     context["object_list"] = Special.objects.all()
#     return context
