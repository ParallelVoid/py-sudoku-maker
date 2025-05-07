from py_sudoku_maker import generate_sudoku
import pytest

"""
    Unit tests to validate that the generated Sudoku board adheres to the standard Sudoku rules:
    
    - Each number from 1 to 9 must appear exactly once in every row.
    - Each number from 1 to 9 must appear exactly once in every column.
    - Each number from 1 to 9 must appear exactly once in each 3x3 subgrid (box).
"""

def test_row():
    full_sudoku = generate_sudoku()
    for sudoku in full_sudoku:
        assert len(set(sudoku)) == 9

def test_col():
    full_sudoku = generate_sudoku()
    for i in range(len(full_sudoku[0])):
        col = []
        for j in range(len(full_sudoku)):
            col.append(full_sudoku[j][i])
        assert len(set(col)) == 9

def test_box():
    full_sudoku = generate_sudoku()
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                full_sudoku[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            assert len(set(box)) == 9


if __name__ == "__main__":
    pytest.main(["-v"])
