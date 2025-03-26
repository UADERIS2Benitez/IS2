#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys

def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

# Verificar si hay argumentos pasados
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Debe ingresar un número válido como argumento.")
        sys.exit()
else:
    try:
        num = int(input("Ingrese un número para calcular su factorial: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        sys.exit()

# Calcular y mostrar el factorial
print("Factorial", num, "! es", factorial(num))
