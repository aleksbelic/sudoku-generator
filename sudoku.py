import random, math, time, winsound, csv

class Sudoku:
    """Some docstring."""
    def __init__(self, size, timer, sound):
        self.size = size
        self.grid = []
        self.timer = timer
        self.sound = sound

    def grid_values_to_list(self):
        """Generates list with grid values."""
        values_list = []
        for row_index in range(self.size):
            for column_index in range(self.size):
                values_list.append(str(self.grid[row_index][column_index]["value"]))
        return values_list
    
    def solve(self):
        """Generates random sudoku grid."""
        print("Generating grid...")
        if self.timer:
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
        if self.timer:
            print("Grid generated in %s sec" % (time.time() - start_time))
        if self.sound:
            winsound.Beep(500, 100)
    
    def check_candidate(self, candidate_row_index, candidate_column_index, candidate):
        """Some docstring."""
        # checking row
        if self.__class__.__name__ == "SudokuGenerator":
            for i in range(candidate_column_index): # candidate_column_index excluded
                if self.grid[candidate_row_index][i]["value"] == candidate:
                    return False
        elif self.__class__.__name__ == "SudokuSolver":
            for i in range(self.size):
                if self.grid[candidate_row_index][i]["value"] == candidate:
                    return False

        # checking column
        if self.__class__.__name__ == "SudokuGenerator":
            for j in range(candidate_row_index): # candidate_row_index excluded
                if self.grid[j][candidate_column_index]["value"] == candidate:
                    return False
        elif self.__class__.__name__ == "SudokuSolver":
            for j in range(self.size): # candidate_row_index excluded
                if self.grid[j][candidate_column_index]["value"] == candidate:
                    return False

        #checking box
        sqrtSize = int(math.sqrt(self.size))
        candidate_box_row_index = int(candidate_row_index / sqrtSize)
        candidate_box_column_index = int(candidate_column_index / sqrtSize)
        for i in range(self.size):
            for j in range(self.size):
                box_row_index = int(i / sqrtSize)
                box_column_index = int(j / sqrtSize)
                if candidate_box_row_index == box_row_index and candidate_box_column_index == box_column_index: # if in the same box
                    if candidate_row_index != i and candidate_column_index != j: # don't compare to itself
                        if candidate == self.grid[i][j]["value"]:
                            return False
        return True # candidate is valid

    def check_grid(self):
        """Checks sudoku grid cell by cell."""
        for row_index in range(self.size):
            for column_index in range(self.size):
                if not self.check_candidate(row_index, column_index, self.grid[row_index][column_index]["value"]):
                    return False
        return True

    def print_grid(self):
        """Prints sudoku grid."""
        sizeSqrt = int(math.sqrt(self.size))
        for row_index in range(self.size):
            # printing horizontal dashes
            if row_index != 0 and row_index % sizeSqrt == 0:
                dashes = ""
                for box_counter in range(sizeSqrt):
                    if box_counter != 0:
                        dashes += "+"
                    for _ in range(sizeSqrt):
                        dashes += "---"
                print(dashes)
            # printing row
            row = ""
            for cell_index, cell in enumerate(self.grid[row_index]):
                if cell_index != 0 and cell_index % sizeSqrt == 0:
                    row += "|"
                row += " " + str(cell["value"]) + " "
            print(row)

class SudokuGenerator(Sudoku):
    """SudokuGenerator class."""
    def __init__(self, size = 9, timer = False, sound = True):
        sqrtSize = math.sqrt(size)
        if (sqrtSize).is_integer():
            self.size = int(size)
        else:
            exit("ERROR: unable to generate grid!\nSquare root of grid size should be an integer and square root of " + str(size) + " is " + str(sqrtSize) + ".\nTry with size 4, 9, 16 etc.")
        self.timer = timer
        self.sound = sound
        self.grid = []
        for row_index in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                self.grid[row_index].append(dict(
                    value = "_",
                    fixed = False,
                    candidates = Helper.get_rand_unique_list(1, self.size),
                ))
        
    def generate(self):
        """Some docstring."""    
        self.solve()

class SudokuSolver(Sudoku):
    """SudokuSolver class."""
    def __init__(self, puzzle_grid = [], timer = False, sound = True):
        sqrtPuzzleGridLen = math.sqrt(len(puzzle_grid))
        if (sqrtPuzzleGridLen).is_integer():
            self.size = int(sqrtPuzzleGridLen)
        else:
            exit("ERROR: incorrect paramater!\nSquare root of grid size should be an integer and square root of " + str(len(puzzle_grid)) + " is " + str(sqrtPuzzleGridLen) + ".")
        self.timer = timer
        self.sound = sound
        self.grid = []
        puzzle_grid_counter = 0
        for row_index in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                if puzzle_grid[puzzle_grid_counter] == 0:
                    self.grid[row_index].append(dict(
                        value = "_",
                        fixed = False,
                        candidates = Helper.get_rand_unique_list(1, self.size),
                    ))
                else:
                    self.grid[row_index].append(dict(
                        value = puzzle_grid[puzzle_grid_counter],
                        fixed = True
                    ))
                puzzle_grid_counter += 1

class Helper:
    """Helper class. Used for additional sudoku methods."""

    @staticmethod
    def get_rand_num(min, max):
        """Returns random integer between min & max (both values included)."""
        return random.randint(min, max)

    @staticmethod
    def get_rand_unique_list(min, max):
        """Returns random list of unique integers between min & max (both values included)."""
        return random.sample(range(min,max + 1), max - min + 1)

    @staticmethod
    def store(sudoku):
        """Stores generated grid to appropriate CSV file. No duplicates will be added."""
        csv_file_name = str(sudoku.size) + "x" + str(sudoku.size) + ".csv"
        csv_file_path = "storage/" + csv_file_name
        try:
            with open(csv_file_path, "r", newline="") as csv_file:
                csv_file_reader = csv.reader(csv_file)
                grid_list = [grid for grid in csv_file_reader]
                if not (sudoku.grid_values_to_list() in grid_list):
                    grid_list.append(sudoku.grid_values_to_list())
                    
            with open(csv_file_path, "w", newline="") as csv_file:
                csv_file_writer = csv.writer(csv_file)
                for grid in grid_list:
                    csv_file_writer.writerow(grid)
        except FileNotFoundError:
            exit("ERROR: sudoku could not be stored, file \"" + csv_file_path + "\" was not found.")

    @staticmethod
    def remove_duplicates_from_storage(csv_file_name):
        """Removes all duplicates from storage file."""
        csv_file_path = "storage/" + csv_file_name
        try:
            with open(csv_file_path, "r", newline="") as csv_file:
                csv_file_reader = csv.reader(csv_file)
                grid_list = [grid for grid in csv_file_reader]
                grid_list_unique = []
                for i in range(0, len(grid_list)):
                    if not grid_list[i] in grid_list_unique:
                        grid_list_unique.append(grid_list[i])
                    
            with open(csv_file_path, "w", newline="") as csv_file:
                csv_file_writer = csv.writer(csv_file)
                for grid in grid_list_unique:
                    csv_file_writer.writerow(grid)
        except FileNotFoundError:
            exit("ERROR: sudoku could not be stored, file \"" + csv_file_path + "\" was not found.")
