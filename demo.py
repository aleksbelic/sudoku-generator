from sudoku import SudokuSolver

#sudoku_example = Sudoku() # size = 9, timer = False, sound = True
#sudoku_example.print_grid()
#Helper.store(sudoku_example) # storing grid to file ./storage/9x9.csv

sudoku_puzzle = [0,0,0,2,6,0,7,0,1,6,8,0,0,7,0,0,9,0,1,9,0,0,0,4,5,0,0,8,2,0,1,0,0,0,4,0,0,0,4,6,0,2,9,0,0,0,5,0,0,0,3,0,2,8,0,0,9,3,0,0,0,7,4,0,4,0,0,5,0,0,3,6,7,0,3,0,1,8,0,0,0,]
sudoku_solver = SudokuSolver(sudoku_puzzle)
#sudoku_solver.solve()
sudoku_solver.print_grid()
