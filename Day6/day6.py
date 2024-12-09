import numpy as np
from collections import defaultdict

data = []
with open(r"Day6\day6_input.txt", 'r') as file:
    for line in file:
        row = list(line.strip())  
        data.append(row)

data = np.array(data)

#Part 1
#Gets the numbers to add to your current coordinate to go in the direction person is facing
def get_coordinate_adder(person: str):
    if person == '^':
        return np.array([-1, 0])
    elif person == 'v':
        return np.array([1, 0])
    elif person == '>':
        return np.array([0, 1])
    elif person == '<':
        return np.array([0, -1])

def get_face(grid):
    if np.any(np.isin(grid, '^')):
        return '^'
    elif np.any(np.isin(grid, 'v')):
        return 'v'
    elif np.any(np.isin(grid, '>')):
        return '>'
    elif np.any(np.isin(grid, '<')):
        return '<'

def rotate_gaurd(grid, gaurd, curr_position):
    positions = ['^', '>', 'v', '<']
    new_face = positions[(positions.index(gaurd) + 1) % 4]

    grid[curr_position[0]][curr_position[1]] = new_face
    return new_face

def is_loop(data, obstruciton_position):
    #Add the obstruciton
    data[obstruciton_position[0]][obstruciton_position[1]] = '#'

    traversed = []
    direction_map = defaultdict(list)

    in_bounds = True
    curr_face = get_face(data)
    indices = np.where(data == curr_face)
    curr_position = np.array([int(indices[0][0]), int(indices[1][0])])
    traversed.append(tuple(curr_position))
    direction_map[tuple(curr_position)].append(tuple(get_coordinate_adder(curr_face)))
    while in_bounds:
        new_position = curr_position + get_coordinate_adder(curr_face)

        if not ((0 <= new_position[0] < data.shape[0]) and (0 <= new_position[1] < data.shape[1])):
            print("out of bounds")
            return False
        elif (data[new_position[0]][new_position[1]] == '#'):
            curr_face = rotate_gaurd(data, curr_face, curr_position)
            direction_map[tuple(curr_position)].append(tuple(get_coordinate_adder(curr_face)))
        else:
            data[new_position[0]][new_position[1]] = curr_face
            curr_position = new_position
            if (tuple(curr_position) in traversed) and (tuple(get_coordinate_adder(curr_face)) in direction_map[tuple(curr_position)]): 
                print("found here")
                return True
            elif tuple(curr_position) not in traversed:
                traversed.append(tuple(curr_position))
                direction_map[tuple(curr_position)].append(tuple(get_coordinate_adder(curr_face)))


#For part 2
data2 = data.copy()

count = 1
traversed = []

#Setup for algorithm
in_bounds = True
curr_face = get_face(data)
indices = np.where(data == curr_face)
curr_position = np.array([int(indices[0][0]), int(indices[1][0])])
traversed.append(tuple(curr_position))

while in_bounds:
    new_position = curr_position + get_coordinate_adder(curr_face)

    if not ((0 <= new_position[0] < data.shape[0]) and (0 <= new_position[1] < data.shape[1])):
        in_bounds = False
    elif (data[new_position[0]][new_position[1]] == '#'):
        curr_face = rotate_gaurd(data, curr_face, curr_position)
    else:
        data[new_position[0]][new_position[1]] = curr_face
        curr_position = new_position
        if tuple(curr_position) not in traversed: 
            count += 1
            traversed.append(tuple(curr_position))


print(count)
obstruction_count = 0

for position in traversed[1:]:
    copy = data2.copy()
    if is_loop(copy, position):
        obstruction_count += 1

print(obstruction_count)

