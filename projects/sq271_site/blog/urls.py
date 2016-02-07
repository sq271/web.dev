from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<url>[-_\w]+)', views.detail, name='detail'),
]
