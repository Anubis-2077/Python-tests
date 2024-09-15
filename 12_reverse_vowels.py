"""
In this kata, your goal is to write a function which will reverse the vowels in a string.
Any characters which are not vowels should remain in their original position. Here are some examples:
"""
s = "Reverse Vowels In A String"

target = ['a', 'e', 'i','o','u','A','E','I','O','U']
list_s = list(s)
    
positions = []

for i in range(len(list_s)):
    if list_s[i] in target:
        positions.append(i)
        
#print("esta es la primera posicion: ", positions)

positions.reverse()

n = 0

for i in range(len(list_s)):
    if list_s[i] in target:
        list_s[i] = list_s[positions[n]]
        n +=1
        
result = "".join(list_s)
print(result)



        