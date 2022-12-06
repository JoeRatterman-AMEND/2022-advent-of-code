# Load required packages
from collections import Counter
import os

# Define input file name
file_name = "day_06.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Convert string to list
input_list = list(input_data[0])

# Define counter
cntr = 0

for i in range(len(input_list)):

    # Update counter
    cntr += 1

    # If > 4 character check if we have unique market
    if i >=4:

        # Create list of last 4 values
        count_list = Counter([input_list[i - 3], input_list[i - 2], input_list[i - 1], input_list[i]])

        # If 4 unique values - break loop 
        if len(list(count_list.keys())) == 4:
            break
    
# Answer #1
print(f"Answer #1: {cntr} characters")

### Problem 2 ----------------------------------------------------------------------------------

# Define counter
cntr = 0

for i in range(len(input_list)):

    # Update counter
    cntr += 1

    # If > 4 character check if we have unique market
    if i >=14:

        # Create list of last 14 values
        msg_list = list(input_list[(i-13):(i+1)])
        print(len(msg_list))
        
        # Create counts of each letter
        count_dict = Counter(msg_list)
 
        # If 14 unique values - break loop 
        if len(list(count_dict.keys())) == 14:
            break

# Answer #2
print(f"Answer #2: {cntr} characters")

    