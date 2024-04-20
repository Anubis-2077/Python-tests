
#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.


def generar_primos(N):
    primos = []
    candidato = 2  # El primer número primo posible

    while len(primos) < N:
        # Comprueba si el candidato es primo
        es_primo = True
        for primo in primos:
            if candidato % primo == 0:
                es_primo = False
                break
            if primo * primo > candidato:
                break
        if es_primo:
            primos.append(candidato)
        candidato += 1

    return primos


cantidad = int(input("Ingrese la cantidad de números primos que desea obtener: "))
print(generar_primos(cantidad))
