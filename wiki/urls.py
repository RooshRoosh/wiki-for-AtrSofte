from django.conf.urls import patterns, include, url
from pages.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiki.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', index),
    url(r'^(?P<page>\w+)/add/$', add_page),
    url(r'^add/$', add_page),
    url(r'^(?P<page>\w+)/edit/$', edit_page),
    url(r'^edit/$', edit_page),
    url(r'^(?P<page>\w+)/delete/$', delete_page),
    url(r'^delete/$', delete_page),
    url(r'^(?P<page>\w+)/$', get_page),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)
