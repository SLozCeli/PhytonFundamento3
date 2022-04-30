def suma_num(n:float, m:float) -> float:
    """Efectúa una suma entre dos valores."""
    while True:
        try:
            st = n+m
            print(f"La suma de {n} + {m} es {st}")
            return(n+m)
        except:
            print("Tipo de dato no válido")
        break

def rest_num(n:float, m:float) -> float:
    """Efectúa una resta de un primer valor menos un segundo valor."""
    while True:
        try:
            r = n-m
            print(f"La resta de {n} - {m} es {r}")
            return(n-m)
        except:
            print("Tipo de dato no válido")
        break

def mult_num(n:float, m:float) -> float:
    """Devuelve el producto entre dos números"""
    while True:
        try:
            float(m)
            float(n)
            p = n * m
            print(f"El producto de {n} * {m} es {p}")
            return(n-m)
        except:
            print("Tipo de dato no válido")
        break

def div_num(n:float, m:float) -> float:
    """Devuelve la división entre dos números"""
    while True:
        try:
            if m == 0:
                print("No se puede dividir entre cero")
            else:
                d = n/m
                print(f"La división de {n} / {m} es {d}")
        except:
            print("Tipo de dato no válido")
        break
