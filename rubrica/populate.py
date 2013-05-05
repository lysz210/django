import string
from django.conf.urls.defaults import *
from django.db import models
from contatti.models import *


f = open("quinta-sa.txt","r")
Testo = f.readlines()
for nome in Testo:
	word = string.split(nome)
	print word

