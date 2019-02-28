import numpy as np
import math

def readSud(sudoku, size):
    sudokulist = list(sudoku)
    sudoku = []
    for i in range(0,size):
        sudoku += [sudokulist[i*size:(i+1)*size]]
    return sudoku

def countpossibilities(sudoku, i, j,size):
    pos = ['1','2','3','4','5','6','7','8','9']
    part = int(math.sqrt(size))
    for k in pos:
        if k in sudoku[i][:] or k in sudoku[:][j]:
            pos.remove(k)
        else:
            begini = int(int(i/part)*part)
            beginj = int(int(j/part)*part)
            for i1 in range(0,3):
                for i2 in range(0,3):
                    if k in sudoku[begini + i1][beginj + i2]:

                        pos.remove(k)
                        print(begini +i1,beginj+ i2)
    return pos

def calculate(sudoku):
    cpos = []
    size = int(math.sqrt(len(sudoku)))
    sudoku = readSud(sudoku, size)
    for i in range(0,size):
        for j in range(0,size):
            if sudoku[i][j] == '.':
                cpos += countpossibilities(sudoku, i, j,size)
    return len(cpos)

print(calculate(".94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8"))
