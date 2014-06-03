from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^collection/', 'viewer.views.index'),
    url(r'^home/', 'viewer.views.homepage'),
    url(r'^create/', 'viewer.views.create'),
    url(r'^request/', 'viewer.views.request'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)