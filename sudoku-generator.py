import time
import random

start_time = time.time()

print("SUDOKU GENERATOR")
table_size = 9
table = []
for i in range(table_size):
    table.append([])
randNum = random.randrange(1, table_size, 1)
print(table)
print("--- %s seconds ---" % (time.time() - start_time))
