"""
2 задача
Да се реализира на python алгоритъм за шифриране на Виженер.
Програмата да приема като входни параметри от командния ред текст и ключ и да извежда шифрирания текст в конзолата. 
Името на изпълнимия файл да е в следния формат: FXXXXX_L3_T2.py, където FXXXXX е вашият факултетен номер.    
"""
import sys

text = sys.argv[1]
key = sys.argv[2]
if (text.find(" ") != -1 ):
    text = text.replace(" ", "")
if (key.find(" ") != -1 ):
    key = key.replace(" ", "")
    
len_txt = len(text)
len_key = len(key)
if len_txt != len_key:
    for i in range(len_txt - len_key):
        key += key[i % len_key]
        
   
ciphered = ""
for i in range(len(text)):
    character = text[i].capitalize()
    
    if (text[i].isupper()):
        ciphered += chr((ord(character) + ord(key[i].capitalize()) ) % 26 + ord('A'))
    else:
        ciphered += chr((ord(character) + ord(key[i].capitalize()) ) % 26 + ord('A')).lower()

            
print(ciphered)