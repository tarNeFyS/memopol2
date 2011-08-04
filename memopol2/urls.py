import os

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import list_detail
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

from votes.models import Proposal

admin.autodiscover()

urlpatterns = patterns('', # pylint: disable=C0103
    url(r'^$', list_detail.object_list, {'queryset': Proposal.objects.all(), 'template_name' : 'home.html'}, name='index'),
    url(r'^europe/parliament/', include('meps.urls', namespace='meps', app_name='meps')),
    url(r'^france/assemblee/', include('mps.urls', namespace='mps', app_name='mps')),
    url(r'^votes/', include('votes.urls', namespace='votes', app_name='votes')),
    url(r'^list/', include('queries.urls', namespace='queries', app_name='queries')),
    url(r'^trends/', include('trends.urls', namespace='trends', app_name='trends')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^contact/', include('contact_form.urls')),
)

# hack to autodiscover static files location in dev mode
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(.*)$', serve, {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
    )
# TODO: static files location in production
# should never be served by django, settings.MEDIA_URL is the right way to do
