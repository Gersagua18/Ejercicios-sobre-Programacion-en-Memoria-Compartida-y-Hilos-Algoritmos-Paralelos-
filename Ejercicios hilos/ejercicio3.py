import threading
import random

datos = [random.randint(1,10) for _ in range(10_000_000)]
suma_total = 0

def sumar_parte(inicio, fin):
    global suma_total
    for i in range(inicio, fin):
        suma_total+=datos[i]
mitad = len(datos) // 2
hilo1 = threading.Thread(target=sumar_parte, args=(0, mitad))
hilo2 = threading.Thread(target=sumar_parte, args=(mitad, len(datos)))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Suma total (sin sincronizacion): {suma_total}")