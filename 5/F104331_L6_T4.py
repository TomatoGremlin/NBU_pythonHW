"""
Задача 4

Напишете рекурсивна функция, която връща дали даден символен низ е палиндром (дали низът и обърнатият символен низ са същите). 
Разпечатвайте True или False в завимиост дали е палиндром."""
import sys

def palindrome_check (string):
    # empty or with 1 character:
    if len(string) < 2: 
        return True
    # 2 or more than characters:
    if string[0] != string[-1]: 
        return False
    return palindrome_check(string[1:-1])

print(palindrome_check(sys.argv[1]))