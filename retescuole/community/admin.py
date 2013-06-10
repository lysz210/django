# admin.py

from django.contrib import admin
from community.models import *
from django import forms

class IscrizioneInline(admin.TabularInline):
    model = Iscrizione

class UtenteOption(admin.ModelAdmin):
    
    def nome_cognome(c):
        return "%s %s" % (c.cognome.title(), c.nome.title())
    nome_cognome.short_description ='Utente'
    
    list_display = ('id_utente', nome_cognome,'scuola_provenienza','luogo_provenienza','email')
    
    #list_filter =('cognome','nome')
    list_per_page = 25
    ordering = ('cognome','nome','luogo_provenienza')
    
    inlines = [IscrizioneInline]


admin.site.register(Gruppo)
admin.site.register(Utente,UtenteOption)
admin.site.register(ModuloFormativo)