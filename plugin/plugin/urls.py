from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plugin.views.home', name='home'),
    # url(r'^plugin/', include('plugin.foo.urls')),

    # Admin urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Application URL
    url(r'plugin/$', 'plugin.plugin_views.index'),
    url(r'', include('plugin.usermanagement.urls')),
)
