import random, math, winsound
#import csv

class Sudoku:
    """Some docstring."""
    def __init__(self, size):
        self.size = size
        self.grid = []
        for row_index in range(self.size):
            self.grid.append([])
            for _ in range(self.size):
                self.grid[row_index].append(dict(
                    value = "_",
                    candidates = Helper.get_rand_unique_list(1, self.size)
                ))

        self.generate_grid()

    #TODO
    def generate_grid(self):
        """Generates random sudoku grid."""
        row_index = 0
        column_index = 0
        while (row_index < self.size):
            
            while True:

                if self.grid[row_index][column_index]["candidates"] == []: # last candidate was false
                    self.grid[row_index][column_index]["candidates"] = Helper.get_rand_unique_list(1, self.size)
                    if column_index != 0:
                        column_index -= 1
                    else:
                        column_index = self.size - 1
                        row_index -= 1
                    break

                else:
                    candidate = self.grid[row_index][column_index]["candidates"][0]
                
                if self.check_candidate(row_index, column_index, candidate) == True: # check candidate
                    self.grid[row_index][column_index]["candidates"].remove(candidate)
                    self.grid[row_index][column_index]["value"] = candidate
                    column_index += 1
                    if column_index == self.size:
                        column_index = 0
                        row_index += 1
                    break
                else:
                    self.grid[row_index][column_index]["candidates"].remove(candidate)
                    if self.grid[row_index][column_index]["candidates"] == []: # last candidate was false
                        self.grid[row_index][column_index]["candidates"] = Helper.get_rand_unique_list(1, self.size)
                        if column_index != 0:
                            column_index -= 1
                        else:
                            column_index = self.size - 1
                            row_index -= 1
                        self.grid[row_index][column_index]["value"] = "_"
                        #return False
        
        winsound.Beep(500, 100)
            
    #TODO
    def check_candidate(self, candidate_row_index, candidate_column_index, candidate):
        # checking row
        for i in range(0, candidate_column_index): # candidate_column_index excluded
            #print(self.grid[candidate_row_index][i]["value"])
            if self.grid[candidate_row_index][i]["value"] == candidate:
                return False
        
        # checking column
        for j in range(0, candidate_row_index): # candidate_row_index excluded
            #print(self.grid[candidate_row_index][i]["value"])
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
                if candidate_box_row_index == box_row_index and candidate_box_column_index == box_column_index:
                    if candidate == self.grid[i][j]["value"]:
                        return False

        return True # OK

    """
    #TODO
    def check_grid(self):
        #Checks sudoku grid.

        # checking rows
        for row_index in range(self.size):
            if len(set(self.grid[row_index])) != self.size: # set removes the duplicates
                return False

        #checking columns
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(self.grid[j][i])
            if len(set(column)) != self.size:
                return False

        #checking boxes
        box_count = int(math.sqrt(self.size))

        return True
    """

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

class Helper:
    """Some docstring"""

    @staticmethod
    def get_rand_num(min, max):
        """Returns random integer between min & max (both values included)."""
        return random.randint(min, max)

    @staticmethod
    def get_rand_unique_list(min, max):
        """Returns random list of unique integers between min & max (both values included)."""
        return random.sample(range(min,max + 1), max - min + 1)
    """
    @staticmethod
    def store(value):
        csv_path = "C:\\xampp\\htdocs\\alex\\sudoku-generator\\grid stash\\9x9.csv"
        csv_obj = open(csv_path, 'a')
        csv_writer = csv.writer(csv_obj)
        csv_writer.writerow(value)
    """

    @staticmethod
    def test():
        for i in range (5, -1, -1):
            print(i)
