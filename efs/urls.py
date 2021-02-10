from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

