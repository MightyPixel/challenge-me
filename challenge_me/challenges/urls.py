from django.conf.urls import patterns
from django.core.urlresolvers import resolve

urlpatterns = patterns('challenges.views',
    (r'^$', 'list'),
    (r'^challenge/(?P<challenge_id>\w+)', 'details'),
    (r'^new', 'new')
)
