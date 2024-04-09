"""  * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". 
 
 
 english
  Write a program that displays (with a print) the
numbers from 1 to 100 (both included and with a line break between
each print), replacing the following:
Multiples of 3 with the word “fizz”.
Multiples of 5 with the word “buzz”.
Multiples of both 3 and 5 with the word “fizzbuzz”. """

def fizzbuzz (n):
    while n < 101:
        if n%3==0 and n%5==0:
            print('fizzbuzz')
        elif n% 3==0:
            print('fizz')
        elif n%5==0:
            print('buzz')
        else:
            print(n)
        n+=1
    return n

fizzbuzz(0)
