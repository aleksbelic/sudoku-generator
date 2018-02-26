import time
from sudoku import SudokuTable, Helper

#start_time = time.time()
table = SudokuTable(9)
table.print_layout()
print(table.check_layout())
#print("--- %s seconds ---" % (time.time() - start_time))

#Helper.test()