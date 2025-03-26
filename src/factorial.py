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
        return f"Factorial de un número negativo ({num}) no existe"
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

def calculate_factorials(start, end):
    for num in range(start, end + 1):
        print(f"Factorial {num} ! es {factorial(num)}")

# Manejo del rango
if len(sys.argv) > 1:
    try:
        user_input = sys.argv[1]
        if '-' in user_input:
            parts = user_input.split('-')
            start = int(parts[0]) if parts[0] else 1  # Si falta el inicio, usar 1
            end = int(parts[1]) if len(parts) > 1 and parts[1] else 60  # Si falta el final, usar 60
        else:
            print("Debe ingresar un rango válido (ejemplo: -10, 4-8, 30-).")
            sys.exit()
    except ValueError:
        print("Debe ingresar un rango válido (ejemplo: -10, 4-8, 30-).")
        sys.exit()
else:
    try:
        user_input = input("Ingrese un rango (ejemplo: -10, 4-8, 30-): ")
        if '-' in user_input:
            parts = user_input.split('-')
            start = int(parts[0]) if parts[0] else 1
            end = int(parts[1]) if len(parts) > 1 and parts[1] else 60
        else:
            print("Debe ingresar un rango válido (ejemplo: -10, 4-8, 30-).")
            sys.exit()
    except ValueError:
        print("Debe ingresar un rango válido (ejemplo: -10, 4-8, 30-).")
        sys.exit()

# Validar el rango
if start > end:
    print("El rango es inválido: el número inicial debe ser menor o igual al final.")
    sys.exit()

# Calcular y mostrar los factoriales
calculate_factorials(start, end)
