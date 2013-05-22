# Create your views here.
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response


def elenco(request):
    contatti = Contatto.objects.all().order_by('cognome')
    return render_to_response('contatti.htm',{'contatti': contatti})
    
def dettagli(request, id) :
    try:
        contatto = Contatto.objects.get(pk=id)
        recapiti = Recapito.objects.filter(appartiene_a=contatto)
        return render_to_response('dettaglio.htm',{'contatto': contatto,'recapiti':recapiti})
    except Contatto.DoesNotExist:
        return HttpResponse("Contatto %s inesistente" % id)