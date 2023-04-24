"""
Напишете програма, която решава квадратно уравнение по зададени коефициенти.
Коефициентите трябва да се приемат като аргумент от командния ред (виж лекция 3).

Програмата трябва да извежда едно от следните неща (без самите кавички):
"x1|x2" - когато има два реални корена, където x1 и x2 са стойностите им
"no real roots" - когато няма реални корени
"x1" - когато има един корен, където x1 е стойността му
"special case" - когато е особен случай

Файлът кръстете FXXXXX_T1.py, където XXXXX е вашият факултетен номер.
"""

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
if a == 0:
    print("special case")
else:
    D = b**2 - 4*a*c
    if D < 0:
        print("no real roots")
    elif D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"{root1:.2f}|{root2:.2f}")
    elif D == 0:
        root1 = -b / (2 * a)
        print(root1)
