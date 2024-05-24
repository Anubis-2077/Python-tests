""" 
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    n = a+b
    
    def to_binary(n):
        while n == 0:
            return "0"
        binary = ""
        while n>0:
            binary = str(n % 2) + binary
            n = n//2
        return binary
    return to_binary(n)



def basic_test_cases():
    assert add_binary(1, 1) == "10", "Test case 1 failed"
    assert add_binary(0, 1) == "1", "Test case 2 failed"
    assert add_binary(1, 0) == "1", "Test case 3 failed"
    assert add_binary(2, 2) == "100", "Test case 4 failed"
    assert add_binary(51, 12) == "111111", "Test case 5 failed"


basic_test_cases()
print("All test cases passed!")