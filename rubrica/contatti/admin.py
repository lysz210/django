from django.contrib import admin
from contatti.models import *
from django import forms


class ContattoAdminForm(forms.ModelForm):
    class Meta:
        model = Contatto
    def clean_cognome(self):
        return self.cleaned_data["cognome"].title()
    def clean_nome(self):
        return self.cleaned_data["nome"].title()
        
class RecapitoOption(admin.ModelAdmin):
    radio_fields={'tipo_del': admin.HORIZONTAL}
    
class RecapitiInline(admin.TabularInline):
    model = Recapito
    

class IndirizziInline(admin.StackedInline):
    model = Indirizzo
	
class AppartenenzaInline(admin.TabularInline):
    model = Appartenenza

# class RubricaOption(admin.ModelAdmin)

class ContattoOption(admin.ModelAdmin):
    
    def nome_cognome(c):
	return "%s %s" % (c.cognome.title(), c.nome.title())
    nome_cognome.short_description ='Contatto'
    
    list_display = (nome_cognome,'cf','data_nascita','sesso')
    
    #list_filter =('cognome','nome')
    list_per_page = 25
    ordering = ('cognome','nome','data_nascita')
    
    form = ContattoAdminForm
    inlines = [RecapitiInline,IndirizziInline,AppartenenzaInline]
    fieldsets = (('Cognome e Nome', {
	'fields': (('cognome','nome'),),
        }),('Dati amministrativi',{
        'fields': ('cf','data_nascita','sesso'),
        'description': '...',
	'classes': ('collapse',),
        }))
    


    
 
admin.site.register(TipoNumero)
admin.site.register(Rubrica)
admin.site.register(Contatto,ContattoOption)
# admin.site.register(Indirizzo)
# admin.site.register(Recapito)
