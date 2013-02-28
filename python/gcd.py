# programma python che calcola il MCD di una coppia di valori

def gcd( a,b ):
	# esco solo se i valori sono uguali
	temp = 0
	r = 0
	print "a    ,b     ,r     ,temp"
	print "------------------------"
	while a!=b:
		if a>b:
			r = a-b
			a=b
			b=r
		else:
			temp=a
			a=b
			b=temp
		# stampo la traccia per aiutare
		print a,"\t",b,"\t",r,"\t",temp
	return a

	
def rgcd(a,b):
	# esco ancora una volta se i valori sono uguali
	print("rgcd( "+str(a)+","+str(b)+" )")
	if a==b:
		return a
	else:
		if a>b:
			return rgcd(b,a-b)
		else:
			return rgcd(b,a)
			
print "Calcolo MCD:"
numero1 = input("Primo numero:")
numero2 = input("Secondo numero:")

print "GCD: "+str(gcd(numero1,numero2))

print "Ora in modo ricorsivo:"
print "GCD: "+ str(rgcd(numero1,numero2))

