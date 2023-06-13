"""
Създайте клас Fibs, реализиращ протокола за итериране.
Следният код трябва да може работи с вашия клас, но да НЕ СЕ съдържа в качения от вас файл.

def main():
    fibs = Fibs()
    for f in fibs:
        if f > 1000:
            print(f)
            break

if __name__ == '__main__':
    main()

Файлът, съдържащ САМО реализирания клас Fibs да се казва FXXXXX_L8_T1.py, където FXXXXX е вашият факултетен номер.  
"""

class Fibs:
    def __init__(self):
        self.previous_num = 0
        self.current_num = 1
        
    def __next__(self):
        nth_fibonacciNumber = self.current_num
        self.current_num = self.previous_num + self.current_num
        self.previous_num = nth_fibonacciNumber
        
        print(nth_fibonacciNumber)
        return nth_fibonacciNumber
    
    def __iter__(self):
        return self
   

