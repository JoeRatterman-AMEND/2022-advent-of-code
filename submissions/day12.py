# Load required packages
from collections import defaultdict, deque
import heapq as heap
import numpy as np
import os

# Define input file name
file_name = "day_12.txt"

# Load input data
file_path = f"C:/Users/{os.getlogin()}/Documents/GitHub/2022-advent-of-code/input-files/{file_name}"
input_data = open(file_path, 'r').read().split('\n')

# Create sequence possible
letter_seq = 'SabcdefghijklmnopqrstuvwxyzE'

# Convert letter seq to list
letter_list = list(letter_seq)

# Create list obj
vert_list = []

# Get list of vertices
for i in range(len(input_data)):
    for j in range(len(input_data[0])):
        vert_list.append(tuple((i,j)))

# Convert data input to matrix
for i in range(len(input_data)):

    if i == 0:
        input_matrix = np.array(list(input_data[i]))
    else:
        input_matrix = np.vstack([list(input_data[i]), input_matrix])

# Flip matrix
input_matrix = np.flipud(input_matrix)

# Replace S & E
for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):

        if input_matrix[i,j] == "S":
            input_matrix[i,j] == "a"
            start_cell = tuple((i,j))

        
        if input_matrix[i,j] == "E":
            input_matrix[i,j] == "z"
            target_cell = tuple((i,j))

# Initialize step check parameters
pair_check = ((0,1), (0,-1), (1,0), (-1, 0))
matrix_len = len(input_matrix[0])
matrix_height = len(input_matrix)

# Create graph dict for results
graph = defaultdict(list)

# Loop through to determine possible paths
for edge in vert_list:

    # Loop through potential neighbors
    for pair in pair_check:
             
            # Find neighbor coordinates
            a, b = edge[0] + pair[0], edge[1] + pair[1]
          
            if a < 0 or b < 0 or a >= len(input_matrix) or b >= len(input_matrix[0]):
                continue
             
            # Check if neighbor is valid coordinate
            if (a >= 0 and b >= 0 and a < matrix_height and b < matrix_len):
              
                # Check if neighbor is viable step
                if letter_list.index(input_matrix[a,b]) - letter_list.index(input_matrix[edge[0], edge[1]]) <= 1:
                
                    graph[tuple((edge[0], edge[1]))].append(tuple((a, b)))


# Define parameters for dijkstra algorithm
startingNode = (start_cell[0],start_cell[1])
visited = set()
parentsMap = {}
nodeCosts = defaultdict(lambda: float('inf'))
nodeCosts[startingNode] = 0
pq = deque()
pq.append((0, start_cell[0],start_cell[1]))

# Create counter
cntr = 0

# Run dijkstra algorithm
while pq:

    # Pull lowest cost
    cost, row, col = pq.popleft()

    # Loop through adjacent nodes
    for adjNode in graph[(row, col)]:
        if adjNode in visited:	continue

        visited.add((adjNode[0], adjNode[1]))
        pq.append((cost + 1, adjNode[0], adjNode[1]))

    # Stop at the target cell
    if target_cell in visited:
      
        break

    # Update counter
    cntr += 1

# Answer #1
print(f"Answer #1: Minimum steps: {cost + 1}.")

### Problem 2 ----------------------------------------------------------------------------------

# Replace S & E
for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):

        if input_matrix[i,j] == "S":
            input_matrix[i][j] == "a"
            start_cell = tuple((i,j))

        
        if input_matrix[i,j] == "E":
            input_matrix[i][j] == "z"
            target_cell = tuple((i,j))


# Initialize step check parameters
pair_check = ((0,1), (0,-1), (1,0), (-1, 0))
matrix_len = len(input_matrix[0])
matrix_height = len(input_matrix)

# Create graph dict for results
graph = defaultdict(list)

# Loop through to determine possible paths
for edge in vert_list:

    # Loop through potential neighbors
    for pair in pair_check:
             
            # Find neighbor coordinates
            a, b = edge[0] + pair[0], edge[1] + pair[1]
          
            if a < 0 or b < 0 or a >= len(input_matrix) or b >= len(input_matrix[0]):
                continue
             
            # Check if neighbor is valid coordinate
            if (a >= 0 and b >= 0 and a < matrix_height and b < matrix_len):
              
                # Check if neighbor is viable step
                if letter_list.index(input_matrix[edge[0], edge[1]]) - letter_list.index(input_matrix[a,b]) <= 1:

                    graph[tuple(((edge[0], edge[1])))].append(tuple((a,b)))


# Define parameters for dijkstra algorithm
startingNode = (target_cell[0],target_cell[1])
visited = set()
parentsMap = {}
nodeCosts = defaultdict(lambda: float('inf'))
nodeCosts[startingNode] = 0
pq = deque()
pq.append((0, target_cell[0],target_cell[1]))

# Create counter
cntr = 0

# Run dijkstra algorithm
while pq:

    # Pull lowest cost
    cost, row, col = pq.popleft()
   
    # Loop through adjacent nodes
    for adjNode in graph[(row, col)]:
        if adjNode in visited:	continue

        # Update visited list & deque
        visited.add((adjNode[0], adjNode[1]))
        pq.append((cost + 1, adjNode[0], adjNode[1]))

    # Stop at the target cell
    if input_matrix[adjNode[0]][adjNode[1]] == "a":
      
        break

    # Update counter
    cntr += 1

# Answer #1
print(f"Answer #2: Minimum steps: {cost}.")
