""" 
Напишете програма, която намира корен на уравнения по метода на дихотомията.
Функцията f(x) да е изнесена в програмна структура функция за леснa промяна.
Числата a и b, които задават интервала на търсене да се въвеждат от клавиатурата.
Числата да се четат като символен низ и след това да се конвертират до число.
Ако въведените от потребителя стойности не са числа, както и ако f(a) и f(b) имат един и същ знак да се пораждат съответни изключения.
Търсенето също да е изнесено във функция с име bisection, която получава три параметъра - a, b и функцията за изчисление f(x).
Функцията bisection трябва да връща резултата с точност 0.001. Тя не трябва да печата нищо.
def f(x):
    return x*x*x+3*x-5

def bisection(a,b, func):
    ...
    ...
    ...
    return ...

print bisection(1,2, f)
Намерете корен на exp(x)-2x-2
Намерете корен на x^3 + 3x-5;
Програмата да е с име FXXXXX_L9_T1.py, където XXXXX е вашият факултетен номер.
"""

import math

class SameSignError(Exception):
    pass

def f(x):
    return x**3 + 3*x - 5   


def bisection( a, b, f ):
    if f(a) * f(b) > 0:
        raise SameSignError("The function values must have opposite signs")

    while abs(b - a) > 0.001:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
    
    return (a + b) / 2


try:
    a = float(input())
    b = float(input())     
except ValueError:
    print("Input is not a number")
else:  
    print(bisection(a, b, f))  
    print(bisection(a, b, lambda x: math.exp(x) - 2*x - 2))
    
    
    
    


