import threading
suma_total = 0
lock = threading.Lock()
def sumar_rango(inicio, fin):
    global suma_total
    suma_parcial = sum(range(inicio, fin))
    with lock:
        suma_total += suma_parcial

n=1_000_000
mitad=n//2
hilo1=threading.Thread(target=sumar_rango, args=(1, mitad+1))
hilo2=threading.Thread(target=sumar_rango, args=(mitad + 1,n+1))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("La suma total de los primeros 1000000 de numeros naturales es:", suma_total)