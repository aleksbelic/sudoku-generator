from sudoku import Sudoku, Helper

sudoku_example = Sudoku() # size = 9, timer = False, sound = True
sudoku_example.print_grid()
Helper.store(sudoku_example) # storing grid to file ./storage/9x9.csv
