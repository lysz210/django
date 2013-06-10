from django.db import models

# Create your models here.

class Gruppo(models.Model):
	id = models.IntegerField(null=False,primary_key=True)
	denominazione = models.CharField(max_length = 20, null=False)
	data_creazione = models.DateField()
	class Meta:
		verbose_name_plural = "Gruppi"
	def __unicode__(self):
		return u"%s %s " % (self.id, self.denominazione)
	
	def get_absolute_url(self):
		return "/gruppi/%i/" % self.id

class Utente(models.Model):
	id_utente = models.IntegerField(primary_key=True)
	nome = models.CharField(max_length = 100)
	cognome = models.CharField(max_length = 100)
	scuola_provenienza = models.CharField(max_length = 200) 
	luogo_provenienza = models.CharField(max_length = 200) 
	email = models.CharField(max_length = 50, null=False,blank=False )
	nome_utente = models.CharField(max_length = 50, null=False,blank=False )
	password = models.CharField(max_length = 50, null=False,blank=False )
	appartiene_a = models.ForeignKey(Gruppo)
	data_creazione = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Utenti"
	def __unicode__(self):
		return u"(%s) %s %s" % (self.nome_utente, self.nome, self.cognome)
		

class ModuloFormativo(models.Model):
	# id automatico
	titolo = models.CharField(max_length = 100, null=False)
	specializzazione = models.CharField(max_length = 100)
	data_creazione = models.DateField()
	rivolto_a = models.ForeignKey(Gruppo)
	iscritti_a = models.ManyToManyField(Utente, through='Iscrizione')
	class Meta:
		verbose_name_plural = "Moduli Formativi"
	def __unicode__(self):
		return u"%s %s (%s)" % (self.id, self.titolo, self.specializzazione)
	
	def get_absolute_url(self):
		return "/ModuliFormativi/%i/" % self.id
	

class Iscrizione(models.Model):
	data_iscrizione = models.DateField(null=False)
	utente = models.ForeignKey(Utente)
	modulo = models.ForeignKey(ModuloFormativo)
	
	class Meta:
		verbose_name_plural = "Iscrizioni"
	def __unicode__(self):
		return u"%s (dal %s)" % (self.utente, self.data_iscrizione)
		
class DocumentoMultimediale(models.Model):
	#id automatico
	titolo = models.CharField(max_length = 100, null=False)
	tipo = models.CharField(max_length = 100, null=False)
	descrizione = models.TextField(null=True)
	data_upload = models.DateField()
	url = models.CharField(max_length = 200, null=False)
	consegnato_per = models.ForeignKey(Iscrizione)
	class Meta:
		verbose_name_plural = "Documenti Multimediali"
	def __unicode__(self):
		return u"%s (%s)" % (self.titolo, self.tipo)
	
	def get_absolute_url(self):
		return "/DocumentiMultimediali/%i/" % self.id
	