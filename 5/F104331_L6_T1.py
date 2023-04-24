""" 
Задача 1

Създайте рекурсивна функция за изчисляване на първите n числа на Фибоначи, и тяхното съхранение в списък. 
Реализацията трябва да съхранява вече изчислените стойности, така че когато рекурсивно извикване е с аргумент, 
който вече е изчислен, стойността да се взима директно, а да не се изчислява.  Програмата с име FXXXXX_L6_T1.py,
където XXXXX е вашият факултетен номер, да получава параметри от командния ред (със sys.argv, не от клавиатурата) 
начално и крайно число позиция в редицата и да разпечатва списък с числата от редицата на Фибоначи, 
от началният до крайният индекс включително.
Примерен изход при параметри 4 20:

[2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

"""
import sys

def fibonacci(nth_number, fibo_list={}):
    if nth_number == 0:
        return []
    elif nth_number == 1:
        return [0]
    elif nth_number == 2:
        return [0, 1]
    elif nth_number in fibo_list:
        return fibo_list[nth_number]
    else:
        current_num = fibonacci(nth_number-1, fibo_list) + [fibonacci(nth_number-1, fibo_list)[-1] + fibonacci(nth_number-2, fibo_list)[-1]]
        fibo_list[nth_number] = current_num
        
        return current_num

start = int( sys.argv[1] ) - 1
end = int( sys.argv[2])
print( fibonacci( end )[start:] )
