from django.contrib import admin
from libreria.models import *

class LibroOption(admin.ModelAdmin):
	# list_display = ('titolo', 'autore', 'genere', 'data_acquisto')
	list_display = ('titolo', 'autore', 'genere', 'data_acquisto', 'modifica_titolo')

admin.site.register(Autore)
admin.site.register(Genere)
admin.site.register(Libro,LibroOption)