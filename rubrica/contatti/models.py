from django.db import models

# Create your models here.


# TipoNumero: Telefono, Fax, Numero Verde, E-MAIL, skype id, ...
class TipoNumero (models.Model):
	descrizione = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Tipo del Numero"
	def __unicode__(self):
		return u"%s" % (self.descrizione)


class Contatto(models.Model):
	nome = models.CharField(max_length = 100)
	cognome = models.CharField(max_length = 100)
	data_nascita = models.DateField(null=True,blank=True)
	# luogo_nascita 
	sesso = models.CharField(blank=True,max_length = 100)
	cf = models.CharField(blank=True,max_length = 16)
	data_creazione = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Contatti"
	def __unicode__(self):
		return u"%s %s" % (self.nome, self.cognome)

class Indirizzo(models.Model):
	etichetta = models.CharField(blank=True,max_length = 100)
	via = models.CharField(max_length = 100)
	localit = models.CharField(blank=True,max_length = 100)
	comune = models.CharField(max_length = 50)
	cap = models.CharField(max_length = 5)
	provincia = models.CharField(max_length = 2)
	nazione = models.CharField(max_length = 50)
	appartiene_a = models.ForeignKey(Contatto)
	class Meta:
		verbose_name_plural = "Indirizzi"
	def __unicode__(self):
		return u"%s %s, %s %s (%s)" % (self.via, self.localit,self.cap,  self.comune, self.provincia )

class Recapito(models.Model):
	appartiene_a = models.ForeignKey(Contatto)
	tipo_del = models.ForeignKey(TipoNumero)
	etichetta = models.CharField(blank=True,max_length = 100)
	numero = models.CharField(max_length = 50)
	class Meta:
		verbose_name_plural = "Recapiti"
	def __unicode__(self):
		if self.etichetta != "":
			return u"%s: %s " % (self.etichetta, self.numero )
		else:
			return u"%s: %s " % (self.tipo_del.descrizione, self.numero )

class Rubrica(models.Model):
	nome = models.CharField(max_length = 100)
	data_creazione = models.DateField()
	membri = models.ManyToManyField(Contatto, through='Appartenenza')
	class Meta:
		verbose_name_plural = "Rubriche"
	def __unicode__(self):
		return u"%s (%s)" % (self.nome, self.data_creazione)

class Appartenenza(models.Model):
	data_iscrizione = models.DateField(auto_now_add=True)
	contatto = models.ForeignKey(Contatto)
	rubrica = models.ForeignKey(Rubrica)
	
