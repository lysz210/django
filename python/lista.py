#!/usr/bin/env python

def swap(x,y):
    return y,x

# boublesort
def bubblesort (lista):
    i=0
    ultimo = len(lista) -1
    ho_scambiato = 1 #true
    while ho_scambiato and ultimo >0:
        ho_scambiato = 0 #false
        while i<ultimo:
            if lista[i]>lista[i+1]:
                #temp = lista[i]
                #lista[i] = lista[i+1]
                #lista[i+1] = temp
                lista[i],lista[i+1] = swap (lista[i],lista[i+1])
                ho_scambiato = 1
            i=i+1
        i=0
        ultimo = ultimo - 1
        
        
lista = []

# Inserisco i dati
x1 = input("Scrivi un numero:")
while x1>0:
    lista.append(x1)
    x1 = input("Scrivi un numero (termina con 0): ")

print "hai inserito: ", len(lista), " elementi"


# Stampo la lista completa
i=0
while i < len(lista):
    print "[", i, "]",lista[i]
    i=i+1

# Ordina la lista
bubblesort(lista)

# Stampo la lista ordinata
i=0
print "Lista ordinata"
while i < len(lista):
    print "[", i, "]",lista[i]
    i=i+1


# Eseguo delle ricerche
x1 = input("cerca nella lista (esci con 0): ")
while x1>0:
    if x1 in lista:
        print "Trovato"
    else:
        print "Non trovato"
    x1 = input("cerca nella lista (esci con 0): ")