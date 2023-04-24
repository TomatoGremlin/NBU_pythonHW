"""
Задача 1
    Напишете програма, което проверява дали даден списък е сортиран. Например за списъка ([1,2,2]) програмата ви трябва да казва, 
    че е сортиран, докато за ('b','a') трябва да казва, че не е сортиран.

    Името на изпълнимия файл да е в следния формат: FXXXXX_L2_T1.py, където FXXXXX е вашият факултетен номер.

    Вход: FXXXXX_L2_T1.py 1 2 2
    Изход: sorted
    Изходът на файла трябва да е една от двете думи sorted или unsorted
"""
import sys

check_list = []
n = len(sys.argv)
for i in range (1, n):
    check_list.append(sys.argv[i])

sorted = 1
for i in range (1, n-1):
    if check_list[i-1] > check_list[i]:
        sorted = 0

if sorted == 1:
    print("sorted")
else:
    print("unsorted")