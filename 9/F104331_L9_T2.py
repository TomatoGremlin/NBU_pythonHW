""" 
Напишете unit test, който тества функцията за изчисление bisection. Преценете сами какви тестове трябва да съдържа.
Програмата да е с име FXXXXX_L9_T2.py, където XXXXX е вашият факултетен номер.
"""
import unittest
import math

class SameSignError(Exception):
    pass

def f(x):
    return x**3 + 3*x - 5   


def bisection( a, b, f ):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError
    if f(a) * f(b) >= 0:
        raise SameSignError

    while abs(b - a) > 0.001:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
    
    return (a + b) / 2


class BisectionTestCase(unittest.TestCase):
    def test_equation1(self):
        result = round(bisection(1, 2, f), 3)
        self.assertAlmostEqual(result, 1.154)

    def test_equation2(self):
        result = round(bisection(0, 2, lambda x: math.exp(x) - 2*x - 2), 3)
        self.assertAlmostEqual(result, 1.678)

    def test_same_sign(self):
        with self.assertRaises(SameSignError):
            bisection(-2, -4, f)

    def test_invalid_a(self):
        with self.assertRaises(ValueError):
            bisection("a", 2, f)

    def test_invalid_b(self):
        with self.assertRaises(ValueError):
            bisection(1, "b", f)

    def test_large_interval(self):
        result = bisection(0, 1000, lambda x: x*x - 5)
        self.assertAlmostEqual(result, 2.236, places=3)


unittest.main()
