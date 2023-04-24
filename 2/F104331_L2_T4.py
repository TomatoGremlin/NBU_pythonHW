"""
Задача 4

Напишете програма, която взима списък от командния ред и прави нов, в който всеки от елементите на първия се среща точно веднъж.
Вход: FXXXXX_L2_T4.py 6 3 7 4 7 4 7 4 8 4 3 8 4 3 8 3 9 4 3
Изход: [3, 4, 6, 7, 8, 9]

Името на изпълнимия файл да е в следния формат: FXXXXX_L2_T4.py, където FXXXXX е вашият факултетен номер.

Изходът трябва да е списък от неповтарящи се елементи
"""
import sys

check_list = []
n = len(sys.argv)
for i in range (1, n):
    check_list.append(sys.argv[i])

no_repeats = []
repeats = 0
for i in range (0, n-1):
    repeats = 0
    for j in range(i+1, n-1):
        if check_list[i] == check_list[j]:
            repeats+=1
    if repeats == 0:
        no_repeats.append(check_list[i])

     
no_repeats.sort()          
print("[", end = '')

for i in range (0, len(no_repeats) ):
    print(no_repeats[i], end = '')
    if i != len(no_repeats) - 1:
        print(", " , end = '')
        
print("]", end = '')