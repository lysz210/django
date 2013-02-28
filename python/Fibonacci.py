#!/usr/bin/env python

# Fibonacci(0)=1
# Fibonacci(1)=1
# Fibonacci(n)=Fibonacci(n-1)+Fibonacci(n-2)
def Fibonacci(n):
    if type(n) == type(1) and n>=0:
        if n==0 or n==1:
            return 1
        else:
            return Fibonacci(n-2)+Fibonacci(n-1)
    else:
        print "Solo numeri interi positivi"
    
n = input("Inserisci un numero:")
print "Il valore della serie di Fibonacci e':", Fibonacci(n)