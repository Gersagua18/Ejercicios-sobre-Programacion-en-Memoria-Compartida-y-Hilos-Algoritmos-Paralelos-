import threading
import random

lista_original=[random.randint(1,1000) for _ in range(1000000)]
sublistas=[]
resultados=[]

num_hilos=4
tamaño_parte=len(lista_original)//num_hilos

def ordenar_parte(sublista, indice):
    resultado=sorted(sublista)
    resultados[indice]=resultado

for i in range(num_hilos):
    inicio=i*tamaño_parte
    fin=(i + 1)*tamaño_parte if i<num_hilos-1 else len(lista_original)
    sublistas.append(lista_original[inicio:fin])
    resultados.append([])

hilos=[]
for i in range(num_hilos):
    hilo=threading.Thread(target=ordenar_parte,args=(sublistas[i],i))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

def fusionar_listas(listas):
    from heapq import merge
    resultado=listas[0]
    for lista in listas[1:]:
        resultado=list(merge(resultado,lista))
    return resultado
#print(lista_ordenada)
lista_ordenada = fusionar_listas(resultados)
print("Lista ordenada:",lista_ordenada == sorted(lista_original))