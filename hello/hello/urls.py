from django.conf.urls import patterns, include, url
from django.contrib import databrowse
from django.contrib.auth.decorators import login_required

from libreria.models import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^hello/', include('hello.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
	
	
	# databrowse
	# url(r'^databrowse/(.*)', databrowse.site.root),
	url(r'^databrowse/(.*)', login_required(databrowse.site.root)),
	

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	# per abilitare delle aree riservate nel sito, attenzione copiare e adattare il template login.html
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^hello/$', "hello.view.hello"),
	url(r'^libri/(\d+)/$', "libreria.views.libro"),
	url(r'^libri/acquistati/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$',"libreria.views.libri_per_data_acquisto"),
	url(r'^libri/autori/(\d+)/$', "libreria.views.libri_autore"),
	url(r'^libri/generi/(\d+)/$', "libreria.views.libri_genere"),
	url(r'^libri/ricerca/$', "libreria.views_wiki.ricerca"),
	url(r'^[l]|[L]ibri/$', "libreria.views.libri"),
)


databrowse.site.register(Genere)
databrowse.site.register(Autore)
databrowse.site.register(Libro)
# databrowse.site.register(Articolo)
