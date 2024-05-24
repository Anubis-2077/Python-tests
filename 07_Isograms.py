""" 
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case."""


def is_isogram(string):
    string = string.lower()  
    letters = list(string)   
    unique_letters = set(letters)  # Crear un conjunto de letras únicas
    
    # Comparar la longitud del conjunto de letras únicas con la longitud de la lista original
    return len(unique_letters) == len(letters)

def basic_test_cases():      
    assert is_isogram("Dermatoglyphics") == True, "Test case 1 failed"
    assert is_isogram("isogram") == True, "Test case 2 failed"
    assert is_isogram("aba") == False, "Test case 3 failed: same chars may not be adjacent"
    assert is_isogram("moOse") == False, "Test case 4 failed: same chars may not be same case"
    assert is_isogram("isIsogram") == False, "Test case 5 failed"
    assert is_isogram("") == True, "Test case 6 failed: an empty string is a valid isogram"

# Ejecutar las pruebas
basic_test_cases()
print("All test cases passed!")


    
