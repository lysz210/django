# admin.py

from django.contrib import admin
from Immobiliare.models import *
from django import forms

#class FotoInline(admin.TabularInline):
#    model = Foto

class AnnuncioInline(admin.StackedInline):
    model = Annuncio

class TipoContrattoOption(admin.ModelAdmin):
    radio_fields={'contratto': admin.HORIZONTAL}
	
class ImmobileOption(admin.ModelAdmin):
    # Mostra al più 25 Immobili per pagina
	list_per_page = 25
	list_display = ('id','nome','via')
	# Mostra l'annuncio nello stesso form dell'immobile
	inlines = [AnnuncioInline]

 
 
admin.site.register(Immobile,ImmobileOption)
admin.site.register(TipoContratto)
admin.site.register(Zona)
admin.site.register(Annuncio)