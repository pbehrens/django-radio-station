from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^post/$', 'content.views.index'),
	url(r'^post/(?P<post_id>\d+)/$', 'content.views.detail'),
    url(r'^post/all/$', 'content.views.all'),

    url(r'^admin/', include(admin.site.urls)),
)