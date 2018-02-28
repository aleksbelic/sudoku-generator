import random, math
#import csv

class Sudoku:
    """Some docstring."""
    def __init__(self, size):
        self.size = size
        self.grid = []
        for _ in range(self.size):
            self.grid.append([])
        self.generate_grid()

    #TODO
    def generate_grid(self):
        """Generates random grid."""
        for row in range(self.size):
            self.grid[row] = Helper.get_rand_unique_list(1, self.size)

    #TODO
    def check_grid(self):
        """Checks grid."""

        # checking rows
        for row in range(self.size):
            if len(set(self.grid[row])) != self.size:
                return False

        #checking columns
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(self.grid[j][i])
            if len(set(column)) != self.size:
                print(set(column))
                return False

        #checking boxes
        box_count = int(math.sqrt(self.size))

        return True

    def print_grid(self):
        """Prints grid."""
        for row in self.grid:
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
        """Just for testing"""
        file = open('./grid stash/9x9.txt', 'a')
        file.write('Test')
        file.close()
