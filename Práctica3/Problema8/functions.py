from random import random

def randoms(l = []) -> list:
    """Genera 20 números aleatorios"""
    l = []
    k = 0
    while k < 20:
        n = int((round(random(), 2))*100)
        l.append(n)
        k += 1
    print("Se ha generado una lista")
    return(l)

def displayrng(o:list) -> str:
    """Muestra la lista de números aleatorios obtenida previamente"""
    if o == []:
        print("No existe una lista generada, pruebe a utilizar randoms() primero.")
    else:
        print(f"La lista generada es {o}")
        

def orgrng(p:list) -> list:
    """Ordena los elementos de la lista randoms() en orden creciente"""
    if p == []:
        print("No existe una lista generada, pruebe a utilizar randoms() primero.")
    else:
        p.sort()
        print(f"La lista en orden creciente es {p}")
       



