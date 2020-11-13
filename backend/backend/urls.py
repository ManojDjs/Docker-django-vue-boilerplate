"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
   
    path('api/accounts/', include('authemail.urls')),
    # url(r'^$',
    #     TemplateView.as_view(template_name='index.html'),
    #     name='index'),

    # url(r'^accounts/',
    #     include('registration.backends.default.urls')),

    # url(r'^accounts/profile/',
    #     TemplateView.as_view(template_name='profile.html'),
    #     name='profile'),

    # url(r'^login/$',
    #     auth_views.LoginView.as_view(
    #         template_name='registration/login.html'),
    #     name='login'),
# url(r'^register/$',
#         auth_views.regs .as_view(
#             template_name='registration/login.html'),
#         name='login'),

    url(r'^admin/',
        admin.site.urls,
        name='admin'),
]