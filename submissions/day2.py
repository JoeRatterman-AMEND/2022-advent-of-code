# Load required packages
import os

# Define input file name
file_name = "day_2.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Define score dict
point_dict = {"X": 1, "Y": 2, "Z": 3}

# Score counter
score = 0

# Loop through each game
for i in range(len(input_data)):

    # Find opponent choice & my choice
    opp, me = input_data[i].split(' ')

    # Calculate points for win, lose, or tie
    round_pts = 0

    # Tie
    if  (opp == "A" and me == "X") or (opp == "B" and me == "Y") or (opp == "C" and me == "Z"): 
        round_pts += 3

    # Win
    elif (opp == "A" and me == "Y") or (opp == "B" and me == "Z") or (opp == "C" and me == "X"): 
        round_pts += 6

    # Loss
    else:
        next

    # Calculate points for my choice
    round_pts += point_dict[me]
    
    # Update overall score
    score += round_pts

# Answer #1
print(f"Answer #1: {score} points")

### Part 2 ----------------------------------------------------------------------------------
# Generate outcome dictionaries
win_dict = {"A":"Y", "B":"Z", "C":"X"}
lose_dict = {"A":"Z", "B":"X", "C":"Y"}
tie_dict = {"A": "X", "B":"Y", "C":"Z"}

# Score counter
score = 0

# Loop through each game
for i in range(len(input_data)):

    # Find opponent choice & my choice
    opp, res = input_data[i].split(' ')

    # Calculate points for win, lose, or tie
    round_pts = 0

    # Determine outcome
    if res == "X": 
        round_pts += point_dict[lose_dict[opp]]
    
    elif res == "Y": 
        round_pts += point_dict[tie_dict[opp]] + 3

    else: 
        round_pts += point_dict[win_dict[opp]] + 6

    # Update overall score
    score += round_pts

# Answer #1
print(f"Answer #2: {score} points")