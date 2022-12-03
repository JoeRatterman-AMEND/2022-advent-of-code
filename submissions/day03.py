# Load required packages
import os
import string

# Define input file name
file_name = "day_03.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Create dictionary for points
lower_dict = dict(zip(string.ascii_lowercase, range(1,27)))
upper_dict = dict(zip(string.ascii_uppercase, range(27,53)))

# Point counter
pts = 0
# Loop through each input
for i in range(len(input_data)):

    # Split string & convert to list of characters
    first, second = list(input_data[i][:len(input_data[i])//2]), list(input_data[i][len(input_data[i])//2:])

    # Find common letter
    common_val = list(set(first) & set(second))

    # Find associated points
    if common_val[0].isupper():

        pts += upper_dict[common_val[0]]
    
    else: 
        pts += lower_dict[common_val[0]]


# Answer #1
print(f"Answer #1: {pts} points")

# Split list into groups
group_list = list(zip(*(iter(input_data),) * 3))

# Point counter
pts = 0
# Loop through each grouping
for i in range(len(group_list)):

    # Split packs for each group
    first, second, third = group_list[i][0], group_list[i][1], group_list[i][2]

    # Find common letter
    common_val = list(set(first) & set(second) & set(third))
    
    # Find associated points
    if common_val[0].isupper():

        pts += upper_dict[common_val[0]]
    
    else: 
        pts += lower_dict[common_val[0]]


# Answer #2
print(f"Answer #2: {pts} points")

