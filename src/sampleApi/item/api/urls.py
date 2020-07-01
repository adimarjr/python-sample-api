from django.conf.urls import url
from .views import (
    ItemAPIView,
    ItemDetailAPIView
)

urlpatterns = [
    url(r'^$', ItemAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ItemDetailAPIView.as_view()),
]