# Load required packages
import os

# Define input file name
file_name = "day_10.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Create result dict
res_dict = {}

# Define cntr
cntr = 1
cyc = 0

# Loop through inputs
for i in range(len(input_data)):

    # Split instructions 
    if (' ' in input_data[i]):
        
        ins, amt = input_data[i].split(" ")
    else:
        ins = input_data[i]

    # Check if noop step
    if ins == "noop":

        # Update results dictionary
        cyc += 1
        res_dict[cyc] = cntr

        continue

    else:

        # Loop through 2 cycles for addition
        for q in range(1,3):

            # Update result dict
            cyc += 1
            res_dict[cyc] = cntr

            if q == 2:

                cntr += int(amt)

            
# Define total val
val = 0

# Loop through key cycles to update value
for q in [20, 60, 100, 140, 180, 220]:

    val += res_dict[q]*q

# Answer #1
print(f"Answer #1: Total strength: {val}.")

### Problem 2 ----------------------------------------------------------------------------------

# Create cycle cntr
cyc = 1

# Create master result list
mast_list = []

# LOop through 6 rows
for q in range(0,6):

    # Create current row result list
    val_list = []

    # Create cntr
    cntr = 0

    # Loop through 40 pixels
    for i in range(0, 40):

        # Check if should be a # or .
        if (cntr == res_dict[cyc] - 1) or (cntr == res_dict[cyc]) or (cntr == res_dict[cyc] + 1):

            val_list.append("#")
        else:
            val_list.append(".")

        # Update counters
        cntr += 1
        cyc += 1

    # Append to master list
    mast_list.append(val_list)

# Answer #2
print(f"Answer #2: Matrix below - easier to paste results into text editor.")
print(mast_list)

