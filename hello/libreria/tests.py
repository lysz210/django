"""
>>> from libreria.models import *
>>> romanzo = Genere(descrizione="romanzo")
>>> romanzo.save()
>>> fantascienza = Genere(descrizione="fantascienza")
>>> fantascienza.save()
>>> giallo = Genere(descrizione="giallo")
>>> giallo.save()
>>>
>>> suskind = Autore(cognome="Suskind", nome="Patrick")
>>> suskind.save()
>>> asimov = Autore(cognome="Asimov", nome="Isaac")
>>> asimov.save()
>>> ellroy = Autore(cognome="Ellroy", nome="James")
>>> ellroy.save()
>>>
>>> profumo = Libro(titolo="Il Profumo",
... genere=romanzo,
... autore=suskind)

>>> profumo.save()
>>>
>>> dalia = Libro(titolo="La dalia nera",
... genere=giallo,
... autore=ellroy)
>>> dalia.save()
>>>
>>> fondazione = Libro(titolo="Fondazione",
... genere=fantascienza,
... autore=asimov)
>>> fondazione.save()
>>>
>>> del Genere.__unicode__
>>>
>>> Genere.objects.all()
[<Genere: Genere object>, <Genere: Genere object>, <Genere: Genere object>]
>>>
>>> for genere in Genere.objects.all():
... 	print genere.descrizione
romanzo
fantascienza
giallo
>>> def __unicode__(self): return self.descrizione
>>> Genere.__unicode__ = __unicode__
>>> Genere.objects.all()
[<Genere: romanzo>, <Genere: fantascienza>, <Genere: giallo>]
>>>
>>> for genere in Genere.objects.all().order_by("descrizione"):
... 	print genere.descrizione
fantascienza
giallo
romanzo
>>>
>>> for autore in Autore.objects.filter(nome="James"):
... 	print autore.nome, autore.cognome
...
James Ellroy
>>>

def form_test():
	r"""
>>> from libreria.views_wiki import *
>>> form = WikisearchForm()
>>> form.as_p()
u'<p>...</ul></p>'
>>> form.as_table()
u'<tr><th>...</td></tr>'
>>> form.as_p()
u'<p><label for="id_autore">...</label></li>\n</ul></p>'
>>> form.fields['autore']
<django.forms.fields.IntegerField object at ...>
>>> form.fields['wikipedia']
<django.forms.fields.CharField object at ...>
>>> form.fields['limite']
<django.forms.fields.IntegerField object at ...>
>>> for field in form.fields:
... 	print field
...
autore
wikipedia
limite
>>>
"""