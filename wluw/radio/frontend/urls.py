from django.conf.urls.defaults import *


urlpatterns = patterns('radio.frontend.views',
    url(r'^$', 'home', name='home'),
	# (r'^about', 'django.views.generic.simple.direct_to_template', {'template': 'frontend/template/about.html'}),

)
