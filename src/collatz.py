
import matplotlib.pyplot as plt

def collatz_iterations(n):
    """
    Calcula el número de iteraciones necesarias para que n
    alcance la secuencia repetitiva (1 -> 4 -> 2 -> 1).
    
    Args:
        n (int): Número inicial.
    Returns:
        int: Número de iteraciones necesarias.
    """
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def main():
    """
    Calcula el número de iteraciones de la secuencia de Collatz
    para los números entre 1 y 10000 y genera un gráfico.
    """
    # Rango de números para calcular la secuencia
    start = 1
    end = 10000

    # Listas para almacenar los datos de graficación
    numbers = list(range(start, end + 1))
    iterations = [collatz_iterations(n) for n in numbers]

    # Configuración del gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(iterations, numbers, s=1, c='blue', alpha=0.7)
    plt.title("Número de Iteraciones de la Secuencia de Collatz")
    plt.xlabel("Número de Iteraciones")
    plt.ylabel("Número Inicial (n)")
    plt.grid(alpha=0.5)
    plt.tight_layout()

    # Guardar y mostrar el gráfico
    plt.savefig("collatz_graph.png")
    plt.show()

if __name__ == "__main__":
    main()
