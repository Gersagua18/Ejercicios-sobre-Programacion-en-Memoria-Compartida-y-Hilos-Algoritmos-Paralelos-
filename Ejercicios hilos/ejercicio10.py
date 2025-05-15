import threading
import random

filas=1000
columnas=1000
matriz1=[[random.randint(1,100) for _ in range(columnas)] for _ in range(filas)]
matriz2=[[random.randint(1,100) for _ in range(columnas)] for _ in range(filas)]
matriz_resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
lock=threading.Lock()

def sumar_fila(i):
    fila_resultado=[]
    for j in range(columnas):
        fila_resultado.append(matriz1[i][j]+matriz2[i][j])
    with lock:
        matriz_resultado[i]=fila_resultado

hilos = []
for i in range(filas):
    hilo=threading.Thread(target=sumar_fila,args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Fila 0 de la matriz resultado:")
print(matriz_resultado[0])