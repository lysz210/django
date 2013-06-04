# Create your views here.

# Create your views here.
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response
from django.utils import timezone


def ElencoClassi(request, anno):
    l_classi = Classe.objects.filter(AS=anno).order_by('corso')
    return render_to_response('classi.htm',{'k_classi': l_classi})

def ElencoClassiAnnoCorrente(request):
    giorno = timezone.now()
    anno = giorno.year
    # correggi se iniziato il nuovo anno
    if giorno.month < 9:
        anno = anno -1 
    return ElencoClassi(request, anno)


def ElencoStudenti(request, id) :
    try:
        o_classe = Classe.objects.get(pk=id)
        l_iscritti = Iscrizione.objects.filter(classe=o_classe)
        return render_to_response('dettaglio.htm',{'k_classe': o_classe,'k_iscritti':l_iscritti})
    except Classe.DoesNotExist:
        return HttpResponse("Classe %s inesistente" % id)
    
def PresenzeMensili(request, id_studente, mese):
    return 0


