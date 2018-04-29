import random, math, time, winsound, csv
from sudoku import Sudoku, Helper

class SudokuGenerator(Sudoku):
    """SudokuGenerator class."""
    def __init__(self, size = 9):
        sqrtSize = math.sqrt(size)
        if (sqrtSize).is_integer():
            self.size = int(size)
        else:
            exit("ERROR: unable to generate grid!\nSquare root of grid size should be an integer and square root of " + str(size) + " is " + str(sqrtSize) + ".\nTry with size 4, 9, 16 etc.")
        self.grid = []
        for row_index in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                self.grid[row_index].append(dict(
                    value = "_",
                    fixed = False,
                    candidates = Helper.get_rand_unique_list(1, self.size),
                ))
    
    def check_candidate(self, candidate_row_index, candidate_column_index, candidate, only_fixed = False):
        """Check if candidate is valid in current cell."""
        # checking row
        for i in range(candidate_column_index): # candidate_column_index excluded
            if self.grid[candidate_row_index][i]["value"] == candidate:
                return False

        # checking column
        for j in range(candidate_row_index): # candidate_row_index excluded
            if self.grid[j][candidate_column_index]["value"] == candidate:
                return False

        #checking box
        sqrtSize = int(math.sqrt(self.size))
        candidate_box_row_index = int(candidate_row_index / sqrtSize)
        candidate_box_column_index = int(candidate_column_index / sqrtSize)
        for i in range(candidate_box_row_index * self.size, (candidate_box_row_index + 1) * sqrtSize):
            for j in range(candidate_box_column_index * self.size, (candidate_box_column_index + 1) * sqrtSize):
                if candidate_row_index != i and candidate_column_index != j: # don't compare to itself
                    if candidate == self.grid[i][j]["value"]:
                        return False
        return True # candidate is valid
        
    def generate(self, timer = False, sound = True):
        """Generates fully solved sudoku grid. Note: generating grid is like solving empty grid."""
        print("Generating grid...")
        if timer:
            start_time = time.time()

        row_index = 0
        column_index = 0
        while (row_index < self.size):
            if self.grid[row_index][column_index]["fixed"] == False:
                while True: 
                    try:
                        candidate = self.grid[row_index][column_index]["candidates"][0]
                    except IndexError: # candidates list is empty
                        self.grid[row_index][column_index]["candidates"] = Helper.get_rand_unique_list(1, self.size)
                        self.grid[row_index][column_index]["value"] = "_"
                        while True:
                            if column_index != 0:
                                column_index -= 1
                            else:
                                column_index = self.size - 1
                                row_index -= 1
                            if self.grid[row_index][column_index]["fixed"] == False:
                                break
                        break
                        
                    if self.check_candidate(row_index, column_index, candidate): # check candidate
                        self.grid[row_index][column_index]["candidates"].remove(candidate)
                        self.grid[row_index][column_index]["value"] = candidate
                        column_index += 1
                        if column_index == self.size:
                            column_index = 0
                            row_index += 1
                        break
                    else:
                        self.grid[row_index][column_index]["candidates"].remove(candidate)
            else:
                column_index += 1
                if column_index == self.size:
                    column_index = 0
                    row_index += 1

        print("Done!")
        if timer:
            print("Grid generated in %s sec" % (time.time() - start_time))
        if sound:
            winsound.Beep(500, 100)
