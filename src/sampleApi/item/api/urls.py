from django.conf.urls import url
from .views import (
    ItemAPIView,
    ItemCreateAPIView,
    ItemDetailAPIView,
    ItemUpdateAPIView,
    ItemDeleteAPIView
)

urlpatterns = [
    url(r'^$', ItemAPIView.as_view()),
    url(r'^create/$', ItemCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ItemDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', ItemUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', ItemDeleteAPIView.as_view()),
]