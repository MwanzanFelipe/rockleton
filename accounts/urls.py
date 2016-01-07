from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views
from django.contrib.auth import views as auth_views



from .views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$', views.register, name = 'register'),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^logout/$', auth.views.logout, name = 'logout'),
]