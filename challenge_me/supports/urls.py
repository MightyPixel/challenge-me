from django.conf.urls import patterns
from django.core.urlresolvers import resolve

urlpatterns = patterns('supports.views',
    (r'^$', 'list'),
    (r'^supporter/(?P<supporter_id>\w+)', 'details')
)
