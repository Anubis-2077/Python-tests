"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"""

def reverse_words(text):
    words = text.split(" ")  
    reversed_words = [word[::-1] for word in words]  
    return " ".join(reversed_words)


print(reverse_words("The quick brown fox jumps over the lazy dog."))