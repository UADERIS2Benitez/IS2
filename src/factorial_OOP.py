#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial_OOP.py                                                        *
# * calcula el factorial de un rango de números                             *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Adaptado a programación orientada a objetos                             *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        """Constructor de la clase Factorial."""
        pass  # No necesita inicializar atributos en este caso

    def calculate(self, num):
        """
        Calcula el factorial de un número dado.
        Args:
            num (int): Número para calcular el factorial.
        Returns:
            int: Factorial del número o mensaje de error si es negativo.
        """
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

    def run(self, min_val, max_val):
        """
        Calcula los factoriales para un rango de números.
        Args:
            min_val (int): Límite inferior del rango.
            max_val (int): Límite superior del rango.
        """
        if min_val > max_val:
            print("El rango es inválido: el número inicial debe ser menor o igual al final.")
            return

        for num in range(min_val, max_val + 1):
            print(f"Factorial {num} ! es {self.calculate(num)}")

# Lógica principal del programa
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            user_input = sys.argv[1]
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

    # Crear instancia de la clase Factorial y ejecutar el método run
    factorial_calculator = Factorial()
    factorial_calculator.run(start, end)
