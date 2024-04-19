#comprueba si una palabra capicua y devuelve una respuesta

#Check if a word is a palindrome and return a response.

def capicua(palabra):
    word = list(palabra)
    word_reverse = list(reversed(word))
    
    if word == word_reverse:
        return True
    else:
        return False

print('this it is gonna be False: ', capicua('amor'))
print('this it is gonna be True: ', capicua('tenet'))
       
       