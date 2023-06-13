""" 
Създайте итеративна реализиция на алгоритъма за обхождане на лабиринт.
Използвайте списък, за да симулирате програмния стек. Създайте функция printMaze, която чертае стените с '#', необходеният път с ' ', 
обходеният в права посока с '.', и в обратна посока с 'x' и целта с 'g'. Когато целта е постигната, използвайте функцията за да разпечатате текущото състояние на лабиринта. 
Функцията за обхождане трябва да се казва solveMaze(x,y) и да приема параметри начални координати на търсенето. 

Файлът трябва да се казва FXXXXX_L8_T2.py, където FXXXXX е факултетният ви номер и да приема от командния ред (със sys.argv) начални координати на търсенето в лабиринта.
"""

import sys

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

def solveMaze(x, y, ):
    stack = [(x, y)]  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        x, y = stack[-1] # top of stack 

        if maze[x][y] == 'g':
            printMaze(maze)  
            break

        if maze[x][y] == ' ': 
             
            maze[x][y] = '.'

            printMaze(maze)
            print('')
            
            for x_change, y_change in directions:
                updatedX = x + x_change
                updatedY = y + y_change
            
                if isCellTraversable(updatedX, updatedY):
                    stack.append((updatedX, updatedY))          
        else:
            maze[x][y] = 'x'
            stack.pop()

  
def isCellTraversable(x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] not in ['#', '.', 'x']:
        return True
    return False


def printMaze(maze):
    for row in maze:
        print(' '.join(row))


x = int(sys.argv[1])
y = int(sys.argv[2])
solveMaze(x, y)



