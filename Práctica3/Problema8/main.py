
from functions import randoms
from functions import displayrng
from functions import orgrng

c_1 = []
v = 0

while True:
    try:
        while True:
            print("""Bienvenido, usuario, por favor, seleccione una opción:
            1) Generar una lista de 20 números aleatorios del 0 al 100
            2) Imprimir la lista de los 20 números aleatorios (se requiere lista previa)
            3) Imprimir la lista en orden creciente de los 20 números aleatorios (se requiere lista previa)
            4) Salir del programa
            """)
            v = int(input("Ingrese el número de acción: "))
            if v == 1:
                c_1 = randoms()
            elif v == 2:
                displayrng(c_1)
            elif v == 3:
                orgrng(c_1)
            elif v == 4:
                print("Finalizó el programa")
                break
            else:
                print("Ocurrió un error, inténtelo de nuevo")
    except:
        print("Ha ocurrido un error")
    break

    