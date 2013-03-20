# Create your views here.
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

# def libri(request):
	# elenco = ""
	# for libro in Libro.objects.all().order_by('titolo'):
		# elenco += "'%s' di %s, %s<br>" % (libro.titolo,libro.autore, libro.genere)
	# return HttpResponse(elenco)


# il parametro {'libri': Libro.objects.all().order_by('titolo')} è un dizionario	
def libri(request): 
	return render_to_response('libri.html', {'libri': Libro.objects.all().order_by('titolo')})

def libro(request, id):
	try:
		libro = Libro.objects.get(pk=id)
		return HttpResponse("'%s' di %s, %s<br>" % (libro.titolo,libro.autore, libro.genere))
	except Libro.DoesNotExist:
		return HttpResponse("Codice %s inesistente" % id)
		
		
def libri_per_data_acquisto(request, mese, anno):
	libri = Libro.objects.filter(data_acquisto__year=int(anno))
	libri = libri.filter(data_acquisto__month=int(mese))
	elenco = ""
	for libro in libri.order_by('titolo'):
		elenco += "'%s' di %s, %s<br>" % (libro.titolo,libro.autore, libro.genere)
	if elenco == "":
		elenco = "Nessun libro"
	return HttpResponse(elenco) 
	
	

def libri_genere(request, id):
	genere = get_object_or_404(Genere, pk=id)
	return render_to_response('libri.html', {'libri': Libro.objects.filter(genere=genere).order_by('titolo'),'genere': genere,})
	
def libri_autore(request, id):
	autore = get_object_or_404(Autore, pk=id)
	return render_to_response('libri.html', {'libri': Libro.objects.filter(autore=autore).order_by('titolo'),'autore': autore,})