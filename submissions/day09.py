# Load required packages
import os

# Define input file name
file_name = "day_09.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Define starting point
h_loc = [500, 500]
t_loc = [500, 500]

# Define direction dict
dir_dict = {"R":(0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

# Define result list
step_list = [(t_loc[0], t_loc[1])]

# Loop through instructions to split direction & step size
for i in range(len(input_data)):

    # Split instructions to direction & step
    dir, step = input_data[i].split(" ")

    # Move through step
    for m in range(int(step)):

        # Calculate new head location
        h_loc = [h_loc[0] + dir_dict[dir][0], h_loc[1] + dir_dict[dir][1]]

        # Calculate two direction tail movements
        # Up right
        if (h_loc[0] - t_loc[0] == 1 and h_loc[1] - t_loc[1] > 1) or (h_loc[0] - t_loc[0] > 1 and h_loc[1] - t_loc[1] == 1):

            t_loc[0] += 1
            t_loc[1] += 1

        # Up left
        if  (h_loc[0] - t_loc[0] == 1 and h_loc[1] - t_loc[1] < -1) or ( h_loc[0] - t_loc[0] > 1 and h_loc[1] - t_loc[1] == -1):

            t_loc[0] += 1
            t_loc[1] -= 1

        # Down right
        if  (h_loc[0] - t_loc[0] < -1 and h_loc[1] - t_loc[1] == 1) or (h_loc[0] - t_loc[0] == -1 and h_loc[1] - t_loc[1] > 1):

            t_loc[0] -= 1
            t_loc[1] += 1

        # Down left
        if  (h_loc[0] - t_loc[0] < -1 and h_loc[1] - t_loc[1] == -1) or (h_loc[0] - t_loc[0] == -1 and h_loc[1] - t_loc[1] < -1):

            t_loc[0] -= 1
            t_loc[1] -= 1

        # Calculate one direction tail movements
        if h_loc[0] - t_loc[0] > 1:
            
            t_loc[0] += 1

        if h_loc[0] - t_loc[0] < -1:

            t_loc[0] -= 1

        if h_loc[1] - t_loc[1] > 1:
            
            t_loc[1] += 1

        if h_loc[1] - t_loc[1] < -1:

            t_loc[1] -= 1
            
        step_list.append(tuple((t_loc[0], t_loc[1])))
       
# Answer #1
print(f"Answer #1: {len(set(step_list))} positions visited.")

### Problem 2 ----------------------------------------------------------------------------------

# Define starting point
h_loc = [500, 500]
t_loc = [500, 500]

# Define direction dict
dir_dict = {"R":(0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

# Define result dict
step_dict = {0:[(t_loc[0], t_loc[1])] , 1:[(t_loc[0], t_loc[1])], 2:[(t_loc[0], t_loc[1])], 3:[(t_loc[0], t_loc[1])], 4:[(t_loc[0], t_loc[1])], 5:[(t_loc[0], t_loc[1])], 6:[(t_loc[0], t_loc[1])], 7:[(t_loc[0], t_loc[1])], 8:[(t_loc[0], t_loc[1])], 9:[(t_loc[0], t_loc[1])]}

# Loop through instructions to split direction & step size
for i in range(len(input_data)):

    # Split instructions to direction & step
    dir, step = input_data[i].split(" ")

    # Move through step
    for m in range(int(step)):

        # Calculate new head location
        h_loc = [step_dict[0][-1][0] + dir_dict[dir][0], step_dict[0][-1][1] + dir_dict[dir][1]]
        step_dict[0].append(tuple((h_loc[0], h_loc[1])))

        # Loop through each knot in the rope
        for q in range(1, len(step_dict.keys())):

            # If looking at knot >=2 need to update the relative head location
            if q >= 2:

                h_loc = [step_dict[q-1][-1][0], step_dict[q-1][-1][1]]

            # Calculate the current value for the knot we're on
            t_loc = [step_dict[q][-1][0], step_dict[q][-1][1]]

            # Calculate two direction tail movements
            # Up right
            if (h_loc[0] - t_loc[0] == 1 and h_loc[1] - t_loc[1] > 1) or (h_loc[0] - t_loc[0] > 1 and h_loc[1] - t_loc[1] == 1):

                t_loc[0] += 1
                t_loc[1] += 1

            # Up left
            if  (h_loc[0] - t_loc[0] == 1 and h_loc[1] - t_loc[1] < -1) or ( h_loc[0] - t_loc[0] > 1 and h_loc[1] - t_loc[1] == -1):

                t_loc[0] += 1
                t_loc[1] -= 1

            # Down right
            if  (h_loc[0] - t_loc[0] < -1 and h_loc[1] - t_loc[1] == 1) or (h_loc[0] - t_loc[0] == -1 and h_loc[1] - t_loc[1] > 1):

                t_loc[0] -= 1
                t_loc[1] += 1

            # Down left
            if  (h_loc[0] - t_loc[0] < -1 and h_loc[1] - t_loc[1] == -1) or (h_loc[0] - t_loc[0] == -1 and h_loc[1] - t_loc[1] < -1):

                t_loc[0] -= 1
                t_loc[1] -= 1

            # Calculate one direction tail movements
            if h_loc[0] - t_loc[0] > 1:
                
                t_loc[0] += 1

            if h_loc[0] - t_loc[0] < -1:

                t_loc[0] -= 1

            if h_loc[1] - t_loc[1] > 1:
                
                t_loc[1] += 1

            if h_loc[1] - t_loc[1] < -1:

                t_loc[1] -= 1
                
            step_dict[q].append(tuple((t_loc[0], t_loc[1])))
       
    
# Answer #2
print(f"Answer #3: {len(set(step_dict[9]))} positions visited.")
 