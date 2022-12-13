# Load required packages
import math
import os

# Define input file name
file_name = r"day_11.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n\n')

# Create monkey item dict
monkey_dict = {}

# Loop through monkeys
for i in range(len(input_data)):

    # Split out monkey detail
    monkey_detail = input_data[i].split('\n')

    # Create dictionary for current monkey
    cur_dict = {}

    # Loop though detail
    for j in range(len(monkey_detail)):

        # Split out different parts of detail
        if j > 0:

            if j == 1:
                
                val_list = monkey_detail[j].split(":")[1].lstrip().split(", ")
                val_list = [int(x) for x in val_list]
                cur_dict[monkey_detail[j].split(":")[0].lstrip()] =  val_list
                
            if j == 2:
                
                cur_dict[monkey_detail[j].split(":")[0].lstrip()] = monkey_detail[j].split(":")[1].lstrip().split(" ")[-2:]

            if j == 3 or j == 4 or j == 5:

                cur_dict[monkey_detail[j].split(":")[0].lstrip()] = int(monkey_detail[j].split(":")[1].lstrip().split(" ")[-1])

        
    # Add results to master list
    monkey_dict[monkey_detail[0]] = cur_dict


# Create result key
res_dict = {}
for k,v in monkey_dict.items():
    res_dict[k] = 0

# Loop through 20 rounds
cntr = 1
while cntr <= 20:

    # Loop through each monkey
    for k,v in monkey_dict.items():

        # Loop through monkey items
        for q in v["Starting items"]:

            new_worry = 0

            # Calculate new worry level
            val = q if v["Operation"][1] == "old" else v["Operation"][1] 

            if v["Operation"][0] == '+':

                new_worry += q + int(val)
            else:

                new_worry += q * int(val)

            # Divide worry by 3
            new_worry = math.floor(new_worry/3)
            
            # Check divisibility
            if new_worry % int(v["Test"]) == 0:
                
                new_monkey = v["If true"]
                monkey_dict[f"Monkey {new_monkey}:"]["Starting items"].append(new_worry)

            else:

                new_monkey = v["If false"]
                monkey_dict[f"Monkey {new_monkey}:"]["Starting items"].append(new_worry)


      
        res_dict[k] += len(v["Starting items"])
        v["Starting items"] = []

    cntr += 1

# Find top 2 results           
res_list = sorted(list(res_dict.values()))[-2:]

# Answer #1
print(f"Answer #1: Inspection points: {res_list[0]*res_list[1]}.")

### Problem 2 ----------------------------------------------------------------------------------

# Create monkey item dict
monkey_dict = {}

# Loop through monkeys
for i in range(len(input_data)):

    # Split out monkey detail
    monkey_detail = input_data[i].split('\n')

    # Create dictionary for current monkey
    cur_dict = {}

    # Loop though detail
    for j in range(len(monkey_detail)):

        # Split out different parts of detail
        if j > 0:

            if j == 1:
                
                val_list = monkey_detail[j].split(":")[1].lstrip().split(", ")
                val_list = [int(x) for x in val_list]
                cur_dict[monkey_detail[j].split(":")[0].lstrip()] =  val_list
                
            if j == 2:
                
                cur_dict[monkey_detail[j].split(":")[0].lstrip()] = monkey_detail[j].split(":")[1].lstrip().split(" ")[-2:]

            if j == 3 or j == 4 or j == 5:

                cur_dict[monkey_detail[j].split(":")[0].lstrip()] = int(monkey_detail[j].split(":")[1].lstrip().split(" ")[-1])

        
    # Add results to master list
    monkey_dict[monkey_detail[0]] = cur_dict

# Create result key
res_dict = {}
for k,v in monkey_dict.items():
    res_dict[k] = 0

# Calculate least common multiple for divisibility check - shoutout johnathanpaulson
lcm = 1
for k,v in monkey_dict.items():

    lcm *= v["Test"]

# Loop through 10000 rounds
cntr = 1
while cntr <= 10000:

    # Loop through each monkey
    for k,v in monkey_dict.items():
       
        # Loop through monkey items
        for q in v["Starting items"]:

            new_worry = 0

            # Calculate new worry level
            val = q if v["Operation"][1] == "old" else v["Operation"][1] 

            if v["Operation"][0] == '+':

                new_worry += q + int(val)
            else:

                new_worry = q * int(val)
            
            # Get remainder of worry & lcm
            new_worry = new_worry % lcm
            
            # Check divisibility
            if new_worry % int(v["Test"]) == 0:
                
                new_monkey = v["If true"]
                monkey_dict[f"Monkey {new_monkey}:"]["Starting items"].append(new_worry)

            else:

                new_monkey = v["If false"]
                monkey_dict[f"Monkey {new_monkey}:"]["Starting items"].append(new_worry)


      
        res_dict[k] += len(v["Starting items"])
        v["Starting items"] = []

    cntr += 1

# Find top 2 results           
res_list = sorted(list(res_dict.values()))[-2:]

# Answer #2
print(f"Answer #2: Inspection points: {res_list[0]*res_list[1]}.")

