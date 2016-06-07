from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
	url(r'^$', 'home'),
	url(r'^(?P<langue>(fr|en))/$', 'home'),
	url(r'^github/$', 'github'),
)