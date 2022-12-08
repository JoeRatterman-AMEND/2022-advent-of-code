# Load required packages
from collections import defaultdict
import os

# Define input file name
file_name = "day_07.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Create list of directories
dir_list = [x.split(" ")[-1] for x in input_data if "dir" in x]

# Create dictionary object 
dir_dict = defaultdict(int)
par_list = []

# Loop through each cmd
for i in range(len(input_data)):

    # Check if it is a list cmd
    if input_data[i] == "$ ls":
        continue

    # Check for change directory command
    if "$ cd" in input_data[i] and input_data[i] != "$ cd ..":
        par_list = par_list + [input_data[i].split(" ")[-1]]

    # If moving backwards remove the directory from par_list
    elif input_data[i] == "$ cd ..":
        par_list.pop()

    if input_data[i].split(" ")[0].isdigit():

        # Current file size
        curr_file_size = int(input_data[i].split(" ")[0])

        # Add file to all parent directories
        for i in range(1, len(par_list)+1):
            dir_dict['/'.join(par_list[:i])] += curr_file_size

# Calculate total dir under 100000
end_list = []
for k,v in dir_dict.items():

    # Check if file size is under 100000
    if v <= 100000:
        
        end_list.append(v)

# Answer #1
print(f"Answer #1: Total size = {sum(end_list)}.")

### Problem 2 ----------------------------------------------------------------------------------

# Calculate space needed
unused_space = 70000000 - dir_dict['/']
space_needed = 30000000 - unused_space

# Loop through dictionary to see which files meet size req
can_del = []
for k,v in dir_dict.items():

    # Check if file is greater than space needed
    if v > space_needed:
        can_del.append(v)

# Sort dictionary
can_del = sorted(can_del)

# Answer #2
print(f"Answer #2: File size = {can_del[0]}.")

