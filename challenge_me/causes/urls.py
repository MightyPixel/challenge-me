from django.conf.urls import patterns
from django.core.urlresolvers import resolve

urlpatterns = patterns('causes.views',
    (r'^$', 'list'),
    (r'^cause/(?P<cause_id>\w+)', 'details'),
    (r'^new', 'new')
)
