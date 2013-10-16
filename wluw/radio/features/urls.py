from django.conf.urls.defaults import *

urlpatterns = patterns('',
    'radio.content.views',
    (r'^$', 'index', name='index'),
    (r'^(?P<post_id>\d+)/$', 'radio.content.views.detail'),
)