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

    #print(k,v)
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

    if v > space_needed:
        can_del.append(v)

# Sort dictionary
can_del = sorted(can_del)

# Answer #2
print(f"Answer #2: File size = {can_del[0]}.")



# # Loop through each step
# for i in range(len(input_data)):

#     # Check if step is looking for files in dir
#     if "$ ls" == input_data[i]:

#         if "$ cd" in input_data[i] and "$ cd .." != input_data[i]:
#             par_list = par_list.append(input_data[i-1].split(" ")[-1])
#         #print(input_data[i-1].split(" ")[-1])

#         # Create temp list for directory objs
#         dir_temp_list = []

#         # Loop through next files until reach next cd
#         for m in range(i, len(input_data)):

#             # If cd then jump back to top loop
#             if "$ cd" in input_data[m]:
#                 break

#             # If direction is not $ ls then add to list
#             if input_data[m] != "$ ls":

#                 # If a sub-dir is contained - just keep letter
#                 if "dir" in input_data[m]:

#                     dir_temp_list.append(input_data[m].split(" ")[-1])
#                 else:
                    
#                     dir_temp_list.append(input_data[m])
        
#         # Add results to dictionary
#         dir_dict[input_data[i-1].split(" ")[-1]] = dir_temp_list
#         if len(par_list) >=2:
#             print(par_list[-2] + '/' + input_data[i-1].split(" ")[-1])
#         print(par_list)

# print(dir_dict)
# # Create file size dict
# val_dict = {}
# # Loop through dir_dict
# for k in dir_dict.keys():

#     val_list = []
#     # Loop through directory files
#     for val in dir_dict[k]:

#         # Check if object is file or directory
#         if val.split(" ")[0].isdigit():
#             val_list.append(int(val.split(" ")[0]))
#         else:
#             val_list.append(val.split(" ")[0])

#     val_dict[k] = val_list

# cntr = 0
# final_dict = {}

# while len(list(final_dict.keys())) < len(list(val_dict.keys())) and cntr < 10000:
#     #print("fd = ", len(list(final_dict.keys())))
#     #print("vd = ", len(list(val_dict.keys())))
#     #print(cntr)
#     for k,v in val_dict.items():
        
#         if all(isinstance(x, int) for x in val_dict[k]) and final_dict.get(k) is None:

#             final_dict[k] = sum(v)

#         else:

#             for val in v:

#                 if val in final_dict.keys():
                    
#                     v.remove(val)
#                     v.append(final_dict[val])

#                     val_dict.update({k:v})
#                 if val == 'dcm':
#                     print("foundit")

#         #print(v)


#            # print(k,v)
    
#     cntr += 1


# # print(list(val_dict.keys()))
# # print(list(final_dict.keys()).sort())

# list_b = sorted(list(final_dict.keys()))
# list_a = sorted(list(val_dict.keys()))


# diff_ab = list(set(list_b) - set(list_a))

# print(diff_ab)
# print(len(list_a))
# print(len(list_b))

# end_list = []
# for k,v in final_dict.items():

#     #print(k,v)
#     if v <= 100000:
        
#         end_list.append(v)


# print(sum(end_list))