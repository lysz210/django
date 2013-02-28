
import math

def AreaDelCerchio(raggio):
	return math.pi * raggio ** 2

def Circonferenza(raggio):
	return math.pi * 2 * raggio

def Diametro(raggio):
	return raggio*2
	
def VolumeDellaSfera(raggio):
	return (4*math.pi)*(raggio ** 3)/3
	
def RaggioDiCirconferenza( cir ):
	raggio = cir / ( 2 * math.pi )
	return raggio

def RaggioDiCerchio( ce ):
	raggio = math.sqrt(ce/math.pi)
	return raggio


	
r = input("Raggio del Cerchio?")
print "Diametro \tCirconferenza \tArea \t\tVolume Sfera" 
print Diametro(r),"\t\t",
print Circonferenza(r),"\t",
print AreaDelCerchio(r),"\t",
print VolumeDellaSfera(r)

c = input( "Circonferenza?: " )
print RaggioDiCirconferenza(c)

c = input("cerchio?") 
print RaggioDiCerchio(c)



 
