#haz una funcion que imprima la tabla de un numero
# make a function that prints the multiplication table of a number

def tabla():
    n = int(input("Ingresa el número para generar su tabla de multiplicar: "))  
    multiplo = 1
    for i in range(1, 11):
        print(f"{n} x {multiplo} = {n * multiplo}")
        multiplo += 1


tabla()

