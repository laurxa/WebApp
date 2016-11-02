from django.conf.urls import url

from .views import *


app_name = 'citation'
urlpatterns = [
    url(r'^$', CitationList.as_view(), name='list'),
    url(r'^create/?$', CitationCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/update/?$', CitationUpdate.as_view(), name='edit'),
    url(r'^(?P<slug>[-\w]+)/?$', CitationDetail.as_view(), name='detail'),
]
