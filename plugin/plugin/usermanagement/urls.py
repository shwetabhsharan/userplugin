from django.conf.urls import patterns, include, url

urlpatterns = patterns('plugin.usermanagement.views',
     url(r'users/view/$', 'view_users'),
    url(r'users/add/$', 'add_user'),
    url(r'users/save/$', 'save_user'),
    url(r'users/$', 'menu'),
)
