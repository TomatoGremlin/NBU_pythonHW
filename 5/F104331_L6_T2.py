""" 
Задача 2
Създайте рекурсивна функция, която при зададено число и степен, връща числото, повдигнато на степента.
Програмата с име FXXXXX_L6_T2.py, където XXXXX е вашият факултетен номер, 
да получава параметри от командния ред  (със sys.argv, не от клавиатурата) 
число и степен и да изпечатва резултатът от повдигането на числото на съответната степен.
Примерен изход при извикване с параметри 2 10:
1024
"""
import sys

def exponentiation(base, power):
    if (power == 0):
        return 1
    elif(power == 1):
        return base
    return exponentiation(base, power - 1) * base

base = int(sys.argv[1])
power = int(sys.argv[2])  
if power < 0:
    power *= -1
    result = 1 / exponentiation(base, power)
else:
    result = exponentiation(base, power)      
print(result)