# Escribe un programa que imprima los 50 primeros números de la sucesión
# * de Fibonacci empezando en 0.
# * - La serie Fibonacci se compone por una sucesión de números en
# *   la que el siguiente siempre es la suma de los dos anteriores.
# *   0, 1, 1, 2, 3, 5, 8, 13...

#Write a program that prints the first 50 numbers of the
#* Fibonacci sequence starting at 0.
#* - The Fibonacci series is composed of a sequence of numbers in
#* which the next one is always the sum of the two previous ones.
#* 0, 1, 1, 2, 3, 5, 8, 13…

def fibonacci():
    try:
        n = int(input("Ingrese el número de elementos de la serie de Fibonacci que desea: "))
    except ValueError:
        print("Por favor, ingrese un número entero.")
        return []

    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_fibonacci = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fibonacci)
    
    return fibonacci_numbers


print(fibonacci())
