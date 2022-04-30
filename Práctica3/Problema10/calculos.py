from operaciones import suma_num
from operaciones import rest_num
from operaciones import mult_num
from operaciones import div_num
print("===Operaciones===")
suma_num(2, 3)
rest_num(7, 2)
mult_num(3, 8)
div_num(12, 24)
print("===Comprobación de errores===")
suma_num("2", 2)
rest_num(0, "asd")
mult_num(3, "d")
div_num("2", 3)
div_num(13, 0)