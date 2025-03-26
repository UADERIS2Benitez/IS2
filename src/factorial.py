#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un rango de números                             *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys

def factorial(num):
    if num < 0:
        return "Factorial de un número negativo no existe"
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

# Función para calcular factoriales en un rango
def calculate_factorials(start, end):
    for num in range(start, end + 1):
        print(f"Factorial {num} ! es {factorial(num)}")

# Verificar si se pasa un argumento
if len(sys.argv) > 1:
    try:
        # Parsear rango desde argumento
        start, end = map(int, sys.argv[1].split('-'))
    except ValueError:
        print("Debe ingresar un rango válido (ejemplo: 4-8).")
        sys.exit()
else:
    try:
        # Solicitar rango al usuario
        user_input = input("Ingrese un rango (ejemplo: 4-8): ")
        start, end = map(int, user_input.split('-'))
    except ValueError:
        print("Debe ingresar un rango válido (ejemplo: 4-8).")
        sys.exit()

# Validar el rango
if start > end:
    print("El rango es inválido: el número inicial debe ser menor o igual al final.")
    sys.exit()

# Calcular factoriales en el rango
calculate_factorials(start, end)
