# programma python che calcola il mcm di una coppia di valori

def mcm( a,b ):
	ma=a
	mb=b
	while ma!=mb:
		if ma>mb:
			mb=mb+b
		else:
			ma=ma+a
	return ma

print "Calcolo mcm:"
numero1 = input("Primo numero:")
numero2 = input("Secondo numero:")

print "Massimo comun divisore: ",mcm(numero1,numero2)

