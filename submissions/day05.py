# Load required packages
from collections import defaultdict, deque, OrderedDict
import os
import re

# Define input file name
file_name = "day_05.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
bins, instructions = open(file_path, 'r').read().split("\n\n")

# Create instructions dictionary
ins_dict = {}
cntr = 0

# Loop through instructions to make dictionary
for i in instructions.splitlines():

    # Split instructions to list
    nums = [int(x) for x in i.split(" ") if x.isdigit()]
    
    # Update dictionary
    ins_dict[cntr] = nums

    # Update counter
    cntr += 1

# Convert input file into dictionary of deques
# Shout out reddit for help with the data import
stacks = defaultdict(deque)
for row in bins.splitlines():
    for i in range(1, len(row), 4):

        # Calculate positioning
        stack = i // 4 + 1

        # If not blank add record to deque
        if row[i] != " ":
                stacks[stack].appendleft(row[i])

# Loop through instructions
for k,v in ins_dict.items():

    # Loop through # of movements
    for i in range(0, v[0]):
        
        aa = stacks[v[1]].pop()

        stacks[v[2]].append(aa)

# Sort dict by stack number
od = OrderedDict(sorted(stacks.items()))

# Create result string
endstr = ""

# Loop through ordered dict
for k, v in od.items():

    endstr += v[-1]

# Answer #1
print(f"Answer #1: The stacks are topped with {endstr}.")

### Problem 2 ----------------------------------------------------------------------------------

# Convert input file into dictionary of deques
stacks = defaultdict(deque)
for row in bins.splitlines():
    for i in range(1, len(row), 4):

        # Calculate positioning
        stack = i // 4 + 1

        # If not blank add record to deque
        if row[i] != " ":
                stacks[stack].appendleft(row[i])

# Loop through instructions
for k,v in ins_dict.items():

    # Temp list to store moves
    temp_stack = []

    # Loop through # of movements
    for i in range(0, v[0]):
        
        # Append temp results
        aa = stacks[v[1]].pop()
        temp_stack.append(aa)
        
    # Reverse list
    temp_stack.reverse()

    # Add results
    for m in range(len(temp_stack)):

        stacks[v[2]].append(temp_stack[m])

# Sort dict by stack number
od = OrderedDict(sorted(stacks.items()))

# Create result string
endstr = ""

# Loop through ordered dict
for k, v in od.items():

    endstr += v[-1]

# Answer #2
print(f"Answer #2: The stacks are topped with {endstr}.")




    