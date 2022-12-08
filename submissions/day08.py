# Load required packages
import bisect
import numpy as np
import os

# Define input file name
file_name = "day_08.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Define list for grid
tree_grid = []

# Convert input to array
for i in range(len(input_data)):
    tree_grid.append([int(x) for x in list(input_data[i])])

# Convert list of lists to numpy
tree_grid = np.array(tree_grid)

# Create list for i,j indices
tall_list = []

# Loop through all rows
for i in range(1, len(input_data) - 1):

    # Loop through all columns
    for j in range(1, len(input_data[i]) -1):

        # Find current tree height
        curr_val = input_data[i][j]

        # Calculate tallest tree in each direction
        tallest_block_a = max(tree_grid[0:i,j])
        tallest_block_b = max(tree_grid[i+1:len(input_data) + 1,j])
        tallest_block_l = max(tree_grid[i,0:j])
        tallest_block_r = max(tree_grid[i,j + 1:len(input_data[i]) + 1])
        
        # If tree is unblocked in one direction, add indices to list
        if int(curr_val) > int(tallest_block_a) or int(curr_val) > int(tallest_block_b) or int(curr_val) > int(tallest_block_l) or int(curr_val) > int(tallest_block_r):

            tall_list = tall_list + [(i,j)]

# Calculate total visible trees
vis_trees = len(input_data)*2 + len(input_data[0])*2 + len(tall_list) - 4

# Answer #1
print(f"Answer #1: {vis_trees} trees visible")

### Problem 2 ----------------------------------------------------------------------------------

# Best visibility score placeholder
best_score = 0

# Loop through all rows
for i in range(1, len(input_data) - 1):

    # Loop through all columns
    for j in range(1, len(input_data[i]) -1):

        # Find current tree height
        curr_val = input_data[i][j]

        # Calculate the visibility above 
        trees_above = list(reversed(tree_grid[0:i,j]))
        block_above = min(next((trees_above.index(n) for n in trees_above if n >= int(curr_val)), len(trees_above)) + 1, len(trees_above))

        # Calculate the visiblity below
        trees_below = list(tree_grid[i+1:len(input_data) + 1,j])
        block_below = min(next((trees_below.index(n) for n in trees_below if n >= int(curr_val)), len(trees_below)) + 1, len(trees_below))

        # Calculate the visibility left
        trees_left= list(reversed(tree_grid[i,0:j]))
        block_left = min(next((trees_left.index(n) for n in trees_left if n >= int(curr_val)), len(trees_left)) + 1, len(trees_left))

        # Calculate the visiblity right
        trees_right = list(tree_grid[i,j + 1:len(input_data[i]) + 1])
        block_right = min(next((trees_right.index(n) for n in trees_right if n >= int(curr_val)), len(trees_right)) + 1, len(trees_right))
       
        # Calculate visibility score
        vis_score = int(block_above)*int(block_below)*int(block_right)*int(block_left)

        # Update highest score
        if vis_score > best_score:
            best_score = vis_score

# Answer #2
print(f"Answer #2: Visibility score: {best_score}.")

