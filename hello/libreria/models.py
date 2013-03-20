from django.db import models

# Create your models here.

class Autore(models.Model):
	nome = models.CharField(max_length=50)
	cognome = models.CharField(max_length=50)
	
	def __unicode__(self):
		return u"%s %s" % (self.nome, self.cognome)
	
	class Meta:
		verbose_name_plural = "Autori"

class Genere(models.Model):
	descrizione = models.CharField(max_length=30)
	
	def __unicode__(self):
		return u"%s" % (self.descrizione)
	class Meta:
		verbose_name_plural = "Generi"

class Libro(models.Model):
	titolo = models.CharField(max_length=200)
	autore = models.ForeignKey(Autore)
	genere = models.ForeignKey(Genere)
	data_acquisto = models.DateField(null=True,verbose_name="data di acquisto")
	
	def __unicode__(self):
		return u"%s (%s)" % (self.titolo, self.genere.descrizione)
	class Meta:
		verbose_name_plural = "Libri"
		
	
	def modifica_titolo(self):
		return (u'<input type="text" name="%s" value="%s" size="30"'
					'class="modifica-titolo">' % (self.pk, self.titolo))
	modifica_titolo.allow_tags = True