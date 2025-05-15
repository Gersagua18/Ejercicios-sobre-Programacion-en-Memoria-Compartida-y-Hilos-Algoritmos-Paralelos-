import threading

numeros=[i for i in range(1,1001)]

suma_total=0
promedio_total=0.0
lock=threading.Lock()

def calcular_suma():
    global suma_total
    suma=sum(numeros)
    with lock:
        suma_total=suma

def calcular_promedio():
    global promedio_total
    promedio=sum(numeros)/len(numeros)
    with lock:
        promedio_total=promedio

hilo_suma=threading.Thread(target=calcular_suma)
hilo_promedio=threading.Thread(target=calcular_promedio)

hilo_suma.start()
hilo_promedio.start()

hilo_suma.join()
hilo_promedio.join()

print(f" Suma total: {suma_total}")
print(f" Promedio: {promedio_total}")