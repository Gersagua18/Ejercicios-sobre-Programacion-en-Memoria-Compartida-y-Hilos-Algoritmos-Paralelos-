import threading
import random

datos=[random.randint(1, 100) for _ in range(1_000_000)]
suma_total=0
lock=threading.Lock()
def calcular_suma(inicio, fin):
    global suma_total
    suma_local = sum(datos[inicio:fin])
    with lock:
        suma_total += suma_local

mitad = len(datos) // 2
hilo1 = threading.Thread(target=calcular_suma, args=(0, mitad))
hilo2 = threading.Thread(target=calcular_suma, args=(mitad, len(datos)))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

media=suma_total/len(datos)
print(f"Media calculada: {media:.2f}") 