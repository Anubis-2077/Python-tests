""" * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama. """
 
""" Write a function that takes two words (String) and returns

true or false (Bool) depending on whether they are anagrams or not.
An Anagram consists of forming a word by reordering ALL
the letters of another initial word.
There is NO need to check that both words exist.
Two exactly identical words are not an anagram.  """
 
 
def anagram (word1, word2):
    if word1 == word2:
        return False
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    if len(word1) != len(word2):
        return False
    
    list_word1 = sorted(list(word1))
    list_word2 = sorted(list(word2))
        
    return list_word1 == list_word2



print('anagram1: ',anagram('listen', 'silent'))

print('anagram2: ',anagram('minimum', 'maximum'))
        
        
        
