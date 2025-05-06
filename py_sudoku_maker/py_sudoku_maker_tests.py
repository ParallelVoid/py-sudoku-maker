from py_sudoku_maker import generate_sudoku
import unittest

class TestSudokuMaker(unittest.TestCase):
    """
    Unit tests to validate that the generated Sudoku board adheres to the standard Sudoku rules:
    
    - Each number from 1 to 9 must appear exactly once in every row.
    - Each number from 1 to 9 must appear exactly once in every column.
    - Each number from 1 to 9 must appear exactly once in each 3x3 subgrid (box).
    """
    def test_row(self):
        full_sudoku = generate_sudoku()
        for sudoku in full_sudoku:
            self.assertEqual(len(set(sudoku)), 9)

    def test_col(self):
        full_sudoku = generate_sudoku()
        for i in range(len(full_sudoku[0])):
            col = []
            for j in range(len(full_sudoku)):
                col.append(full_sudoku[j][i])
            self.assertEqual(len(set(col)), 9)

    def test_box(self):
        full_sudoku = generate_sudoku()
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(full_sudoku[box_row + i][box_col + j])

                with self.subTest(box_start=(box_row, box_col)):
                    self.assertEqual(len(set(box)), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
