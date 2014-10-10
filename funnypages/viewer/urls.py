from django.conf.urls import patterns, url
from viewer.views import LandingPageView

urlpatterns = patterns('',
    url(r'^$', LandingPageView.as_view(), name='landingpage'),
    url(r'^edit/(?P<collection_id>\d+)/$', 'viewer.views.edit', name='edit'),
    url(r'^create/$', 'viewer.views.create', name='create'),
    url(r'^collection/(?P<collection_id>\d+)/$', 'viewer.views.viewer', name='viewer'),
)
