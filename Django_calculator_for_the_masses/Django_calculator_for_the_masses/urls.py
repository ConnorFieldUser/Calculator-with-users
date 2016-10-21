"""Django_calculator_for_the_masses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# Why don't you like the imports lined up?
from calculator.views import UserCreateView, OperationView, OperationCreateView, ProfileDetailView, \
                             ProfileUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', OperationCreateView.as_view(), name="operation_create_view"),
    url(r'^operation/$', OperationView.as_view(), name="operation"),
    url(r'accounts/profile/$', ProfileUpdateView.as_view(), name="profile_view"),
    url(r'^profiles/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name="profile_detail_view")
]
