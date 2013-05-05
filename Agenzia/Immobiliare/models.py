from django.db import models

# Create your models here.
# TipoNumero: Telefono, Fax, Numero Verde, E-MAIL, skype id, ...
class Zona (models.Model):
	localit = models.CharField(max_length=50)
	comune = models.CharField(max_length=50)
	cap = models.CharField(max_length = 5)
	provincia = models.CharField(max_length = 2)
	nazione = models.CharField(max_length = 50)
	
	class Meta:
		verbose_name_plural = "Zone geografiche"
	def __unicode__(self):
		return u"%s (%s)" % (self.localit, self.comune)


# TipoNumero: Telefono, Fax, Numero Verde, E-MAIL, skype id, ...
class TipoContratto (models.Model):
	descrizione = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Tipo del contratto"
	def __unicode__(self):
		return u"%s" % (self.descrizione)

		
class Immobile(models.Model):
	nome = models.CharField(blank=True,max_length = 100)
	via = models.CharField(max_length = 100)
	zona = models.ForeignKey(Zona)
	# Esempi di "verbose name"
	numero_stanze = models.IntegerField("Numero delle stanze",null=True)
	numero_bagni = models.IntegerField("Numero dei bagni",null=True)
	numero_camere = models.IntegerField("Numero delle camere",null=True)
	metri_quadrati = models.IntegerField("Superficie commerciale",null=False)
	class Meta:
		verbose_name_plural = "Immobili"
	def __unicode__(self):
		return u"%s %s, %s %s (%s)" % (self.via, self.zona.localit,self.zona.cap,  self.zona.comune, self.zona.provincia )
		
class Annuncio(models.Model):
	riferimento = models.CharField(max_length = 5, primary_key=True)
	etichetta = models.CharField(blank=True,max_length = 100)
	descrizione = models.TextField(max_length=50)
	riferito_a = models.ForeignKey(Immobile)
	contratto = models.ForeignKey(TipoContratto)
	data_pubblicazione = models.DateField("pubblicato il")
	prezzo = models.DecimalField(max_digits=10,decimal_places=2)
	class Meta:
		verbose_name_plural = "Annunci Immobiliari"
	def __unicode__(self):
		return u"%s %s" % (self.riferimento, self.riferito_a )
		
class Foto(models.Model):
	didascalia = models.CharField(blank=True,max_length = 100)
	# url = models.ImageField(upload_to="immagini")
	immobile = models.ForeignKey(Immobile)
		