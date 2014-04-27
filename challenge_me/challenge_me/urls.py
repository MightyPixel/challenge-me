from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'challenges.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),

    url(r'^causes/', include('causes.urls')),
    url(r'^challenges/', include('challenges.urls')),
    url(r'^supports/', include('supports.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
