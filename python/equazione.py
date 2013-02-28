#!/usr/bin/env python

import math

def Delta(a,b,c):
    return b**2 - 4*a*c

def soluzione( a,b,c ):
    d = Delta(a,b,c)
    if d>0:
        x1 = (-b-math.sqrt(d))/(2*a)
        print "Soluzione 1:", x1
        x2 = (-b+math.sqrt(d))/(2*a)
        print "Soluzione 2:", x2
    elif d==0:
        x1 = -b/(2*a)
        print "Soluzioni coincidenti:", x1
    else:
        print "Non ci sono soluzioni. Il determinante e' negativo:", d

valore_a = input("Inserisci il coefficiente di x quadro: a =")
valore_b = input("Inserisci il coefficiente di x: b =")
valore_c = input("Inserisci il termine noto c =")


soluzione (valore_a,valore_b,valore_c)



