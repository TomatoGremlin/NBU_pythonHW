"""
Задача 3

Напишете програма, която взима списък и проверява дали който и да е от елементите му се повтаря повече от веднъж.
Вход: FXXXXX_L2_T3.py 5 3 1 5 9 2 8 6 7
Изход: True

Името на изпълнимия файл да е в следния формат: FXXXXX_L2_T3.py, където FXXXXX е вашият факултетен номер.

Входните данни приемайте като параметри от командния ред (виж слайдове "Параметри от командния ред" на презентация 3), а не четете от клавиатурата с input/raw_input

Изходът трябва да е булева стойност, ако има повтарящи се елементи True, False в противен случай
"""
import sys

check_list = []
n = len(sys.argv)
for i in range (1, n):
    check_list.append(sys.argv[i])

repeats = 0
for i in range (0, n-1):
    for j in range(i+1, n-1):
        if check_list[i] == check_list[j]:
            repeats+=1
            
if repeats != 0:
    print("True")
else:
    print("False")