import threading
import random

lista1=[random.randint(1, 10) for _ in range(1000)]
lista2=[random.randint(1, 10) for _ in range(1000)]

producto_total=0
lock=threading.Lock()

def producto_parcial(inicio,fin):
    global producto_total
    producto=0
    for i in range(inicio,fin):
        producto+=lista1[i]*lista2[i]
    with lock:
        producto_total+=producto

medio=len(lista1)//2
hilo1=threading.Thread(target=producto_parcial,args=(0,medio))
hilo2=threading.Thread(target=producto_parcial,args=(medio,len(lista1)))

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Producto escalar total:",producto_total)