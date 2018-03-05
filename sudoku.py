import random, math
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
                    value = None,
                    candidates = list(range(1, self.size + 1)) #Helper.get_rand_unique_list(1, self.size)
                ))

        self.generate_grid()

    #TODO
    def generate_grid(self):
        """Generates random sudoku grid."""
        for row_index in range(self.size):
            for column_index in range(self.size):

                for candidate_index, candidate in enumerate(self.grid[row_index][column_index]["candidates"]):
                    if self.check_candidate(row_index, column_index, candidate) == True: # check candidate
                        self.grid[row_index][column_index]["value"] = candidate
                        break

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
