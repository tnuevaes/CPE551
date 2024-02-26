# Author: Teddy Nueva Espana
# Date: 2/23/24
# I pledge my honor that I have abided by the Stevens honor system
# Description: This program generates a two dimensional list and generates random values
# for each element in the list. The program iterates through the list finding the lowest
# and highest value and their respective coordinates in the grid and displays the grid

import random

SIZE = 8

grid = [[0 for i in range(SIZE)] for h in range (SIZE)]


for x in range(len(grid)):
    for i in range(len(grid)):
        grid[x][i] = random.randint(0,500)

high_x = 0
high_y = 0
low_x = 0
low_y = 0

high_cap = grid[0][0]
low_cap = grid[0][0]

for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] > high_cap:
            high_cap = grid[y][x]
            high_x = x + 1
            high_y = y + 1 
        elif grid[y][x] < low_cap:
            low_cap = grid[y][x]
            low_x = x + 1 
            low_y = y + 1 
            

print(f"Highest capture rate: {high_cap} at coordinates: {high_x} , {high_y}")
print(f"Lowest capture rate: {low_cap} at coordinates: {low_x} , {low_y}")

print("The map is as follows:")
for row in grid:
        for element in row:
            print(format(element, '3'), end='  ')
        print()