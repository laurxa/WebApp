from django.conf.urls import url
from django.contrib.auth.views import logout_then_login

from .views import *


app_name = 'user'

urlpatterns = [
    url(r'^register/?$', Register.as_view(), name='register'),
    url(r'^login/?$', custom_login, name='login'),
    url(r'^logout/?$', logout_then_login, name='logout'),
]
