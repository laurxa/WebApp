from django.conf.urls import url

from .views import *


app_name = 'user'

urlpatterns = [
    url(r'^login/?$', Login.as_view(), name='login'),
]
