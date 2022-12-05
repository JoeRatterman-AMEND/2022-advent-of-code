# Load required packages
import os

# Define input file name
file_name = "day_04.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Occurence counter
cntr = 0

# Loop through each input
for i in range(len(input_data)):

    # Split first & second range
    first, second = input_data[i].split(",")

    # Min / max of first range
    first_min, first_max = map(int, first.split("-"))

    # Min / max of second range
    second_min, second_max = map(int, second.split("-"))

    # Check if range is contained in other range
    if (first_min >= second_min) & (first_max <= second_max):

        cntr += 1
    
    elif (second_min >= first_min) & (second_max <= first_max):

        cntr += 1

# Answer #1
print(f"Answer #1: {cntr} overlaps")

### Problem 2 ----------------------------------------------------------------------------------

# Occurence counter
cntr = 0

# Loop through each input & check for any overlap
for i in range(len(input_data)):

    # Split first & second range
    first, second = input_data[i].split(",")

    # Min / max of first range
    first_min, first_max = map(int, first.split("-"))

    # Min / max of second range
    second_min, second_max = map(int, second.split("-"))

    # Convert ranges to lists
    first_range = list(range(first_min, first_max + 1))
    second_range = list(range(second_min, second_max + 1))

    # Check for common values
    aa = list(set(first_range) & set(second_range))

    # If common values exist increase counter
    if len(aa) > 0:
        cntr += 1
  
# Answer #2
print(f"Answer #2: {cntr} overlaps")


