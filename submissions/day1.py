# Load required packages
import numpy as np
import os


# Define input file name
file_name = "day_1.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Define empty dict
cal_dict = {}

# Define elf counter
elf = 0
cal_tot = 0

# Loop through each elf adding calories to elf
for i in range(len(input_data)):

    # Move to next elf if blank record appears
    if input_data[i] == "": 

        # Update counters
        elf += 1
        cal_tot = 0

        print("Next Elf")

    else: 

        # Update total calories in elf's pack
        cal_tot += int(input_data[i])
        cal_dict[elf] = cal_tot

# Convert elf calorie totals to list
cal_list = list(cal_dict.values())

# Answer #1
print(f"Answer #1: {max(cal_list)} calories")

# Sort list descending
cal_list.sort(reverse = True)

# Answer #2
print(f"Answer #2: {sum(cal_list[0:3])} calories")

