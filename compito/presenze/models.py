from django.db import models

# Create your models here.


class Studente(models.Model):
	matricola = models.CharField(max_length = 6, primary_key=True)
	nome = models.CharField(max_length = 100)
	cognome = models.CharField(max_length = 100)
	data_nascita = models.DateField(null=True,blank=True)
	luogo_nascita = models.CharField(max_length = 100) 
	sesso = models.CharField(blank=True,max_length = 100)
	cf = models.CharField(blank=True,max_length = 16)
	email = models.CharField(max_length = 50, null=True,blank=True )
	telefono = models.CharField(max_length = 50, null=True,blank=True )
	cellulare = models.CharField(max_length = 50, null=True,blank=True )
	data_creazione = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name_plural = "Studenti"
	def __unicode__(self):
		return u"(%s) %s %s" % (self.matricola, self.nome, self.cognome)

class Presenza(models.Model):
	studente = models.ForeignKey(Studente)
	data_ora_ingresso = models.DateTimeField(null=False)
	data_ora_uscita = models.DateTimeField(null=True, blank=True)
	note = models.TextField(null=True)
	class Meta:
		verbose_name_plural = "Presenze"
	def __unicode__(self):
		return u"(%s) %s, %s " % (self.studente.matricola, self.data_ora_ingresso, self.data_ora_uscita )
		
class Classe(models.Model):
	AS = models.IntegerField(null=False)
	corso = models.CharField(max_length = 10, null=False)
	specializzazione = models.CharField(max_length = 100)
	data_creazione = models.DateField()
	membri = models.ManyToManyField(Studente, through='Iscrizione')
	class Meta:
		verbose_name_plural = "Classi"
	def __unicode__(self):
		return u"%s %s (%s)" % (self.AS, self.corso, self.specializzazione)
	
	def get_absolute_url(self):
		return "/classe/%i/" % self.id
	

class Iscrizione(models.Model):
	data_iscrizione = models.DateField(null=False)
	studente = models.ForeignKey(Studente)
	classe = models.ForeignKey(Classe)
	
	class Meta:
		verbose_name_plural = "Iscrizioni"
	def __unicode__(self):
		return u"%s (dal %s)" % (self.classe, self.data_iscrizione)