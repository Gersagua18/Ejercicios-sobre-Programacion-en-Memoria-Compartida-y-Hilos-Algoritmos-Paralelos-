import threading

numeros=list(range(2, 10001))
primos=[]
lock=threading.Lock()
def es_primo(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def contar_primos():
    for numero in numeros:
        if es_primo(numero):
            with lock:
                primos.append(numero)

def sumar_primos():
    while True:
        with lock:
            if len(primos)==len([n for n in numeros if es_primo(n)]):
                suma=sum(primos)
                print(f"Suma de números primos: {suma}")
                break

hilo1 = threading.Thread(target=contar_primos)
hilo2 = threading.Thread(target=sumar_primos)
hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Numeros primos encontrados: {len(primos)}")