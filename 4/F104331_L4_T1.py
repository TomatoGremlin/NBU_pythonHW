"""
Напишете програма, която извежда списък от всички ключове, които сочат към дадена стойност, а ако няма нито една такава стойност, то да се връща празен списък. 
Програмата да приема като входен параметър стойността за търсене. 
Речникът да е статично описан в кода на програмата и да е следния: d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'} 
Името на изпълнимия файл да е в следния формат: FXXXXX_L4_T1.py, където FXXXXX е вашият факултетен номер.

Примерен изход:

[1, 4, 7]
"""
import sys

d = {1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'} 
value = sys.argv[1]
keys = []
for i, val in d.items(): 
    if  val == value :
        keys.append(i)
        
print (keys)