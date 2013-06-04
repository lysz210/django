from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compito.views.home', name='home'),
    # url(r'^compito/', include('compito.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # url(r'^classi/', include('compito.presenze.ElencoClassi')),
    url(r'^classi/$', 'presenze.views.ElencoClassiAnnoCorrente'),
    url(r'^classi/(\d{4})$', 'presenze.views.ElencoClassi'),
    url(r'^classe/(\d+)/$', 'presenze.views.ElencoStudenti'),
    
    url(r'studente/(\v+)/(\d{2})$','presenze.views.PresenzeMensili'),
    url(r'classe/presenze/(\d+)/)
    
    
)
