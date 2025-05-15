import threading
import queue
import time
import random

tareas=queue.Queue()
for i in range(1,21):
    tareas.put(i)

lock=threading.Lock()

def procesar_tarea():
    while not tareas.empty():
        try:
            tarea=tareas.get(timeout=1)
        except queue.Empty:
            break
        resultado=tarea**2
        with lock:
            print(f"Hilo {threading.current_thread().name} procesó tarea {tarea} → resultado: {resultado}")
        tareas.task_done()
        time.sleep(random.uniform(0.1,0.3))

hilos=[]
for i in range(5):
    hilo=threading.Thread(target=procesar_tarea,name=f"Hilo-{i+1}")
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las tareas fueron procesadas.")