from django.conf.urls import url
from django.contrib.auth.views import login


app_name = 'user'

urlpatterns = [
    url(r'^login/?$', login, name='login'),
]
