from django.conf.urls import url

from .views import *


app_name = 'citation'
urlpatterns = [
    url(r'^$', CitationList.as_view(), name='list'),
]
