"""estate URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from estateapp.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
