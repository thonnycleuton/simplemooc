from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details')
)