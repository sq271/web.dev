from django.conf.urls import patterns, include, url
from pastebin.views import list, detail, about, new_paste, index

urlpatterns = patterns('',
    url(r'^list/', list),
    url(r'^about/', about),
    url(r'^new/', new_paste),
    url(r'^(?P<url>[a-f*\d*]+)', detail),
)
