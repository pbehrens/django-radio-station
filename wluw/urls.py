
from django.conf.urls.defaults import patterns, include, handler500, handler404
from django.conf import settings
from django.contrib import admin
import d51_django_admin_piston

handler500 = 'radio.frontend.views.server_error'

admin.autodiscover()
d51_django_admin_piston.autodiscover(admin.site)

urlpatterns = patterns(
    '',
	(r'^grappelli/', include('grappelli.urls')),
    (r'^logs/', include('radio.logs.urls')),
    (r'^events/', include('radio.events.urls')),
    (r'^station/', include('radio.station.urls')),
    (r'^staff/', include('radio.staff.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^', include('radio.frontend.urls')),
	(r'^admin/filebrowser/', include(admin.site.urls)),
	(r'^admin/', include(admin.site.urls)),
	(r'^tinymce/', include('tinymce.urls')),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
	            'document_root': settings.MEDIA_ROOT,
	        }),
	#post urls
	(r'^post/$', 'radio.content.views.index'),
	(r'^post/(?P<post_id>\d+)/$', 'radio.content.views.detail'),
    (r'^post/all/$', 'radio.content.views.all'),
	# #csvImporterstuff
	# (r'^$', 'csv_list', name='csv-list'),
	# url(r'^new/$', 'new', name='new-csv'),
	# url(r'^(?P<object_id>\d+)/$', 'associate', name='associate-csv'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
