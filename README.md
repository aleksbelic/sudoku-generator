# sudoku-solver

Sudoku-solver is a simple, terminal-based app programmed in Python 3. It can be used for both solving and generating sudoku puzzles.

### Usage

All examples are located inside **demo.py** file.

### Solving sudoku puzzle
Solving a puzzle is done using **SudokuSolver** class. Constructor params:
- **puzzle_grid**, list, puzzle values placed inside a list with **0** in place where puzzle cell is empty, default is [] (empty list)
- **timer**, boolean, defines if time should be measured, default is false
- **sound**, boolean, defines if completion should be followed by a sound, default is true
```
sudoku_puzzle = [0,0,5,0,1,0,0,0,0,0,2,0,4,0,0,0,0,1,0,9,0,5,0,0,0,8,0,5,0,8,0,0,0,3,0,0,0,7,2,0,4,0,1,6,0,0,0,6,0,0,0,7,0,2,0,5,0,0,0,1,0,2,0,7,0,0,0,0,8,0,3,0,0,0,0,0,3,0,6,0,0,]
sudoku_solver = SudokuSolver(sudoku_puzzle) # sudoku_puzzle, timer = False, sound = True
sudoku_solver.solve()
sudoku_solver.print_grid()
```
Output:
```
Generating grid...
Done!
 6  4  5 | 8  1  7 | 2  9  3
 8  2  3 | 4  9  6 | 5  7  1
 1  9  7 | 5  2  3 | 4  8  6
---------+---------+---------
 5  1  8 | 6  7  2 | 3  4  9
 9  7  2 | 3  4  5 | 1  6  8
 4  3  6 | 1  8  9 | 7  5  2
---------+---------+---------
 3  5  4 | 9  6  1 | 8  2  7
 7  6  1 | 2  5  8 | 9  3  4
 2  8  9 | 7  3  4 | 6  1  5
```

### Generating new puzzle

Generating new puzzle is done using **SudokuGenerator** class. Constructor params:
- **size**, integer, defines grid size, default is 9
- **timer**, boolean, defines if time should be measured, default is false
- **sound**, boolean, defines if completion should be followed by a sound, default is true
```
sudoku_example = SudokuGenerator() # size = 9, timer = False, sound = True
sudoku_example.generate()
sudoku_example.print_grid()
```
Output:
```
Generating grid...
Done!
 6  9  1 | 2  7  4 | 5  8  3
 7  3  5 | 9  6  8 | 1  2  4
 4  2  8 | 3  5  1 | 6  9  7
---------+---------+---------
 9  8  4 | 5  2  6 | 3  7  1
 2  6  7 | 1  8  3 | 9  4  5
 5  1  3 | 7  4  9 | 2  6  8
---------+---------+---------
 1  5  6 | 4  9  7 | 8  3  2
 3  4  9 | 8  1  2 | 7  5  6
 8  7  2 | 6  3  5 | 4  1  9
```

### Storing generated puzzles
Storing new puzzle is done using a **Helper** class. All puzzles are stored in **storage** folder as comma separated values according to their grid size: 4x4 to 4x4.csv file, 9x9 to 9x9.csv etc. Only unique grids will be stored, duplicates will be ignored.
```
sudoku_example = SudokuGenerator() # size = 9, timer = False, sound = True
sudoku_example.generate()
Helper.store(sudoku_example) # storing grid to file ./storage/9x9.csv
```
