# admin.py

from django.contrib import admin
from presenze.models import *
from django import forms

class IscrizioneInline(admin.TabularInline):
    model = Iscrizione

class StudenteOption(admin.ModelAdmin):
    
    def nome_cognome(c):
        return "%s %s" % (c.cognome.title(), c.nome.title())
    nome_cognome.short_description ='Studente'
    
    list_display = ('matricola', nome_cognome,'cf','data_nascita','sesso','email','telefono','cellulare')
    
    #list_filter =('cognome','nome')
    list_per_page = 25
    ordering = ('cognome','nome','data_nascita')
    
    inlines = [IscrizioneInline]


admin.site.register(Classe)
admin.site.register(Studente,StudenteOption)
admin.site.register(Presenza)