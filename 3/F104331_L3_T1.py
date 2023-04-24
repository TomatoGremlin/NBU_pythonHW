"""
1 задача
Да се реализира на python алгоритъм за шифриране на Цезар. 
Програмата да приема като входни параметри от командния ред текст и ключ и да извежда шифрирания текст в конзолата.
Името на изпълнимия файл да е в следния формат: FXXXXX_L3_T1.py, където FXXXXX е вашият факултетен номер.    
"""

import sys

text = sys.argv[1]
key = int(sys.argv[2])

ciphered = ""
for i in range(len(text)):
    character = text[i]
    
    if character.isalpha() == True:
        if (character.isupper()):    
            ciphered += chr((ord(character) + key - ord('A')) % 26 + ord('A'))
        else:
            ciphered += chr((ord(character) + key - ord('a')) % 26 + ord('a'))
    else:
        ciphered += character
        

print(ciphered)
