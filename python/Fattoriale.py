#!/usr/bin/env python

def Fattoriale(n):
    if n==0:
        return 1
    else:
        return n * Fattoriale(n-1)
        
    
x1 = input("Inserisci un numero:")
y1 = Fattoriale(x1)
print "Il fattoriale vale:", y1



