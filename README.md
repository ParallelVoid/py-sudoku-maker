# py-generator

A Python package for generating Sudoku puzzles.

The **sudoku-generator** package provides an easy-to-use interface for generating a valid, fully solved Sudoku puzzle board. Whether you're building a Sudoku game or simply need a solved puzzle for testing or educational purposes, this package offers a convenient solution. The generated Sudoku boards follow the standard 9x9 grid layout with numbers ranging from 1 to 9, ensuring that each puzzle is fully solved and meets the rules of the game.

## Key Features:

- **Generates a Fully Solved Sudoku Board**: Quickly create a completed, valid Sudoku grid with no conflicts.
- **Fast and Efficient**: The package uses an optimized backtracking algorithm for generating and solving puzzles.
- **No External Dependencies**: Lightweight and easy to install with no complex dependencies.

## How to Use:
- Import py_generator
- If you just want to generate a matrix for a sudoku board, call the `generate_sudoku()` function
- If you want to print a complete sudoku board in your command line, call the `print_sudoku()` function
