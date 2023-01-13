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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
schema_view = get_schema_view(
   openapi.Info(
      title="DRF Registration API",
      default_version='v1',
      description="DRF Registration",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('drf_registration.urls')),
    path('Aggregator/', include('Aggregator.api.urls')),
    # path('FQA/', include('FPrograms.api.urls')),
    path('USER/', include('users.api.urls')),
    path('Course/', include('Courses.api.urls')),
    # path('Questions/', include('Questions.api.urls')),
    # path('Demo/',include('Demographics.api.urls')),
    # path('MWB/',include('MentalWellbeing.api.urls')),
    # path('FMWB/',include('FMentalWellbeing.api.urls')),
    # path('WBMNU/',include('WellbeingModelNU.api.urls')),
    # path('FWBMNU/', include('FWellbeingModelNU.api.urls')),

    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)