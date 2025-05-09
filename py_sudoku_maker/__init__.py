"""Functions for the py_sudoku_maker package"""

import random


def generate_sudoku() -> list[list[int]]:
    """Function that generates a 9x9 matrix sudoku solution"""
    sudoku = [[],[],[],[],[],[],[],[],[]]
    sudoku = fill_line(sudoku)
    sudoku = fill_rest_rows(sudoku)
    sudoku = shuffle_sudoku(sudoku)
    return sudoku

def fill_line(sudoku: list[list[int]]) -> list[list[int]]:
    """
    Helper function that fills the first row in sudoku board
    Input: empty 9x9 matrix
    Returns 9x9 matrics with one row filled
    """
    nums = [1,2,3,4,5,6,7,8,9]
    while len(nums) != 0:
        if len(nums) > 1:
            temp = nums[random.randint(1, len(nums) - 1)]
            sudoku[0].append(temp)
            nums.remove(temp)
        else:
            temp = nums[0]
            sudoku[0].append(temp)
            nums.remove(temp)

    return sudoku

def fill_rest_rows(sudoku: list[list[int]]) -> list[list[int]]:
    """
    Helper function that fills the rest of the rows in the matrix
    Input: semi-empty matrix (only one row filled)
    Returns filled 9x9 matrics
    """
    for i in range (1, 9):
        if i%3 == 0:
            for j in range(0, 9):
                if j+1 == 9:
                    sudoku[i].append(sudoku[i-1][0])
                else:
                    sudoku[i].append(sudoku[i-1][j+1])
        else:
            for j in range(0, 9):
                if j+3 >= 9:
                    sudoku[i].append(sudoku[i-1][j-6])
                else:
                    sudoku[i].append(sudoku[i-1][j+3])

    return sudoku

def shuffle_sudoku(sudoku: list[list[int]]) -> list[list[int]]:
    """Helper function that shuffles the sudoku board"""
    swap1 = [1,2,3,4,5,6,7,8,9]
    swap2 = [1,2,3,4,5,6,7,8,9]

    while len(swap1) != 0 and len(swap2) != 0:
        if len(swap1) > 1:
            num1 = swap1[random.randint(1, len(swap1) - 1)]
            swap1.remove(num1)
            num2 = swap2[random.randint(1, len(swap2) - 1)]
            swap2.remove(num2)
        else:
            num1 = swap1[0]
            num2 = swap2[0]
            swap1.remove(num1)
            swap2.remove(num2)
        for i in range(0,9):
            temp1 = sudoku[i].index(num1)
            temp2 = sudoku[i].index(num2)
            sudoku[i][temp1] = num2
            sudoku[i][temp2] = num1

    return sudoku

def print_sudoku():
    """Function that prints the sudoku board in a CLI"""
    sudoku = generate_sudoku()
    out = ["","","","","","","","",""]
    for i, row in enumerate(sudoku):
        for j, s in enumerate(row):
            out[i] += str(s)
            if (j + 1) % 3 == 0:
                out[i] += "  "
            else:
                out[i] += " "

    for line, o in enumerate(out):
        print(o)
        if (line + 1) % 3 == 0:
            print("")
