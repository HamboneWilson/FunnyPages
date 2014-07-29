from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'viewer.views.landingpage', name='landingpage'),
    url(r'^edit/$', 'viewer.views.edit', name='edit'),
    url(r'^create/$', 'viewer.views.create', name='create'),
    url(r'^collection/(?P<collection_id>\d+)/$', 'viewer.views.viewer', name='viewer'),
)
