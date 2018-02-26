import random, math

class SudokuTable:
    """Some docstring."""
    def __init__(self, size):
        self.size = size
        self.layout = []
        for _ in range(self.size):
            self.layout.append([])
        self.generate_layout()

    #TODO
    def generate_layout(self):
        """Generates random sudoku table layout."""
        for row in range(self.size):
            self.layout[row] = Helper.get_rand_unique_list(1, self.size)

    #TODO
    def check_layout(self):
        """Checks sudoku table layout."""

        # checking rows
        for row in range(self.size):
            if len(set(self.layout[row])) != self.size:
                return False

        #checking columns
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(self.layout[j][i])
            if len(set(column)) != self.size:
                print(set(column))
                return False

        #checking regions
        region_count = int(math.sqrt(self.size))

        return True

    def print_layout(self):
        """Prints sudoku table layout."""
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

    @staticmethod
    def test():
        """Just for testing"""
        col = [9,8,7,7,6]
        print(set(col))
