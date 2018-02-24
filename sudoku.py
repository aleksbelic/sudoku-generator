import random

class SudokuTable:
    """Some docstring."""
    
    def __init__(self, size):
        self.size = size
        self.layout = []
        for _ in range(self.size): # underscore is for unused variable
            self.layout.append([])

    def print_layout(self):
        """Printing the sudoku table."""
        for row in self.layout:
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
