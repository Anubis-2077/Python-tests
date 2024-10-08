"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be assumed 
to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

from collections import Counter

def duplicate_count(text):
    lowercase_text = text.lower()
    count = Counter(lowercase_text)
    result=0
    for _,value in count.items():
        if value > 1:
            result +=1
    
    return result
    
print(duplicate_count('Indivisibilities')) #2