"""Define String.prototype.toAlternatingCase (or a similar function/method such 
as to_alternating_case/toAlternatingCase/ToAlternatingCase ) 
such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:"""

def to_alternating_case(string):
    word = ""
    for i in string:
        if i.isupper():
           i = i.lower()
        else:
           i = i.upper()
        word += i
    return word