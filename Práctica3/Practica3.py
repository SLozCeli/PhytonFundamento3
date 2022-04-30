#Problema N°1:
def count_lword(texto = ""):
    """Cuenta la longitud de la última palabra en un texto"""
    texto = str(input("Ingrese un texto: "))
    texto = texto.lstrip()
    texto = texto.rstrip()
    lword = (texto.rpartition(" "))
    while True:
        if len(lword[2]) == 0:
            print("Ingrese un texto válido")
            count_lword(texto = "")
        else:
            print(f"la longitud de la última palabra es {len(lword[2])}")
        break
count_lword()

#Problema N°2:
def ttext(texto = ""):
    """Convierte en mayúscula las primeras letras de cada palabra en un texto"""
    texto = str(input("Ingrese un texto: "))
    texto = texto.lstrip()
    texto = texto.rstrip()
    ctext1 = texto.rsplit(" ")
    ctext2 = []
    while True:
        if len(texto) == 0:
            print("Ingrese un texto válido")
            ttext(texto = "")
        else:
            for i in ctext1:
                i = i.capitalize()
                ctext2.append(i)
            print(" ".join(ctext2))
        break
ttext()

#Problema N°3:
pi = 3.14
class CIRCULO:
    def __init__(self, radio:float) -> None:
        self.radio = radio
        area = 2 * radio * pi
        print(f"El área del círculo con radio {radio} es {area}")
        pass
circulo1 = CIRCULO(3)
print(circulo1)

#Problema N°4:
class RECTANGULO:
    def __init__(self, alto:float, ancho:float) -> None:
        self.alto = alto
        self.ancho = ancho
        arear = alto * ancho
        print(f"El área del rectángulo de altura {alto} y anchura {ancho} es {arear}")
        pass
rectangulo1 = RECTANGULO(4, 5)

#Problema N°5:
class Alumno:
    def __init__(self, nombre:str, nregis:int) -> None:
        self.nombre = nombre
        self.nregis = nregis
    def Display(self):
        print(f"Nombre de estudiante: {self.nombre}, número de registro: {self.nregis}")
    def setAge(self, edad:int):
        print(f"la edad del alumno {self.nombre} es de {edad} años")
    def setNota(self, nota:float):
        print(f"La nota del alumno {self.nombre} es de {nota}")
        pass
alumno1 = Alumno("Alberto Vega", 102412)
alumno1.Display()
alumno1.setAge(19)
alumno1.setNota(17.5)

#Problema N°6:
def list_nota(listnota = ""):
    """Devuelve una lista de notas redondeadas hacia arriba"""
    listnota = input("Ingrese la lista decimal de notas, con una coma y espacio entre cada nota: ")
    listnota = listnota.lstrip()
    listnota = listnota.rstrip()
    ln1 = listnota.rsplit(", ")
    ln2 = []
    ln3 = []
    while True:
        try:
            for i in ln1:
                if i != ", ":
                    i = float(i)
                    ln2.append(i)
            for i in ln2:
                if i - int(i) >= 0.5:
                    ln3.append(int(i+1))
                else:
                    ln3.append(int(i))
            print(f"La lista de notas redondeadas es: {ln3}")
        except:
            print("Ingrese una lista válida")
            list_nota()
        break
list_nota()

#Problema N°7:
def pascal(n:int = 1):
    """Forma una pirámide de Pascal"""
    while True:
        try:
            n = int(input("Ingresar un número: "))
            c = 1
            for i in range(1, n+1):
                for e in range(1, n-i+1):
                    print(" ",end="")
                for j in range(0, i):
                    if j != 0:
                        c = c * (i - j)//j
                    print(c, end=" ")
                print()
        except:
            print("Ingrese un número válido")
            pascal()
        else:
            break
pascal()


