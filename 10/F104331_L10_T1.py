'''
Създайте програма, която отваря текстов файл и му сортира редовете, записвайки сортираните редове в друг файл. 
Програмата с име FXXXXX_L10_T1.py, където XXXXX е вашият факултетен номер, 
да получава параметри от командния ред (със sys.argv, не от клавиатурата) име на файл за сортиране 
и име на файл за записване на резултата.
'''

import sys

def sort_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    sorted_lines = sorted(lines)

    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)

input_file = sys.argv[1]
output_file = sys.argv[2]
sort_file(input_file, output_file)

