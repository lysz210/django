# Il dizionario e' un tipo di dato primitivo, fondamentale,  
# a mappatura di Python.


# Il diszionario e' on oggetto a composto da valori individuati da una chiamve
{ "dict_key": "valore arbitrario di qualunque tipo, compreso funzioni" }

# per la creazione ci sono differenti tecniche, quello sopracitato(letterale)
esempio = {
            "key": "Ciao mondo!"
          }
print esempio
type( esempio )

# Oltre a questo si puoi richiamare direttamente la classe nativa di Python che lo
# rappresenta con differenti parametri da passare
# esempio preso dalla guida ufficiale http://docs.python.org/2/library/stdtypes.html
# a passaggio di argomenti
a = dict(one=1, two=2, three=3)
# Una lista i cui elementi sono liste a 2 elementi qui viene usato la funzione nativa zip
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
l1 = ['one', 'two', 'three']
l2 = [1, 2, 3]
l1_l2 = zip(l1, l2)
print l1_l2
# simile all'esempio precendente dove gli elementi lista vengono sostituiti da tuple
d = dict([('two', 2), ('one', 1), ('three', 3)])
# usando un'altro dizionario
e = dict({'three': 3, 'one': 1, 'two': 2})
# sembra inutile ma potrebbe tornare utile perche' non e' un riferimento al dict in argomento
prova1 = { 'ciao': "mondo" }
prova2 = prova1
id(prova1) # allocazioe di a ( identificativo )
id(prova1) == id(prova2)  # True
prova3 = dict(prova1)
id(prova1) == id(prova3)   # False
a == b == c == d == e   #True

# Per poter accedere ai valori del dizionario si deve usare la notazione come con la lista
# usando la key al posto dell'indice, infatti se si volese usare degli interi si avrebbe una specie di lista
print "a['one'] =", a['one']

# esisto anche dei metodi di accesso rapido ai valori e chiavi
# keys() restituisce tutte le chiavi
d_keys = a.keys()
print 'key of a', d_keys
d_values = a.values()
print 'valori di a:', d_values
# items() si ottiene una lista di tuple(key, value) molto comodo per iterarli
for k,v in a.items():
  print k, '=', v

# I dizionari sono oggeti mutevoli per cui
del a['one']    # elimina la il valore con la key
# Quando si tenta di richiamare con una chiave non valida restituisce un errore
a['one']
# per aggiungere
a['uno'] = 1
# questo sistema e' molto pratico per riempire dizionari anche vuoti
temp = {}
for k, v in zip(l1, l2):
  print k, v
  temp[k] = v
print temp
# un altro metodo molto importante e' update, esegue un merge di 2 dict
# dal momento che a == b == True
print a
a.update(b)
print a    # non e' cambiato nulla
temp = { "mykey": "my value" }
a.update(temp)
print a
# nel caso esistano valori con la stessa chiave, il valore del chiamante verra' sovrascritto
b["one"] = "nuovo valore"
a.update(b)
print a


