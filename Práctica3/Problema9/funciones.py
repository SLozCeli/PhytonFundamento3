from random import random
def juego_adivinar(a = 0):
    """Inicia un juego de adivinanza de un número entre 1 y 100. el número 101 indica rendición"""
    n = 0
    while n == 0:
        n = int((round(random(), 2))*100)
    while True:
        try:
            a = int(input("Ingrese un número entero entre 1 y 100: "))
            if a == 101:
                print("¡Usted se ha rendido!")
            elif 0 > a or a > 100:
                print("Por favor, se lo ruego, ingrese un número válido")
                juego_adivinar()
            elif a == n:
                print("Felicidades, usted ha ganado")
            elif a > n or n > a:
                print("Número incorrecto, vuelva a intentarlo")
                juego_adivinar()
        except ValueError:
            print("Ingrese un número válido")
            juego_adivinar()
        break