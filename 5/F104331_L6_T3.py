"""
Задача 3
Напишете рекурсивна функция за двоично търсене в нареден списък. Програмата с име FXXXXX_L6_T3.py, където XXXXX е вашият факултетен номер, 
да получава параметър от командния ред  (със sys.argv, не от клавиатурата) число за търсене. Резултатът е един от следните два:
not found - ако стойността не се намира в списъка
found at X - ако първото срещане на търсената стойност в списъка е на позиция X
Списъкът за търсене да е статично описан в кода и да е следният:
[30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]

Примерен изход при подаване на параметър 88999999

not found

Примерен изход при подаване на параметър 584

found at 54
"""

import sys

def binary_search(arr , search_value, start_id, end_id):
    if (search_value < arr[start_id]  or search_value > arr[end_id]):
        print("not found")
        return
   
    mid_id = int( (start_id + end_id)/ 2 )
    
    if search_value == arr[mid_id]:
        print(f"found at {mid_id}") 
    elif search_value > arr[mid_id]:
        return binary_search(arr, search_value, mid_id + 1, end_id)
    else:
        return binary_search(arr, search_value, start_id , mid_id - 1)
    
s = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]
end = len(s) - 1
binary_search(s, int(sys.argv[1]), 0 , end)  