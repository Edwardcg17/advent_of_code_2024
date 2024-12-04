import numpy as np

WORDLENGTH = 4

with open("Day4/day4_input.txt", 'r') as file:
    lines = file.readlines()

data = np.array([list(line.strip()) for line in lines])
height = data.shape[1]
width = data.shape[0]

#Part 1
#Indexes to add to go in that direction
directions = {
    "right": (0, 1),
    "left": (0, -1),
    "down": (1, 0),
    "up": (-1, 0),
    "top-right": (-1, 1),
    "top-left": (-1, -1),
    "bottom-right": (1, 1),
    "bottom-left": (1, -1)
}


def check_directions(y, x, directions, data):
    count = 0
    for direction in directions.values():
        dy = direction[0]
        dx = direction[1]
        word = [data[y + k * dy][x + k * dx] for k in range(WORDLENGTH) if (0 <= y + k * dy < data.shape[0] and 0 <= x + k * dx < data.shape[1])]

        if 'XMAS' in ''.join(word):
            count += 1
    return count

def check_x(y, x, data):
    letters = []
    if not (0 <= y + directions["top-left"][0] < data.shape[0] and 0 <= x + directions["top-left"][1] < data.shape[1]):
        return False
    letters.append(data[y + directions["top-left"][0]][x + directions["top-left"][1]])
    if not (0 <= y + directions["top-right"][0] < data.shape[0] and 0 <= x + directions["top-right"][1] < data.shape[1]):
        return False
    letters.append(data[y + directions["top-right"][0]][x + directions["top-right"][1]])
    if not (0 <= y + directions["bottom-left"][0] < data.shape[0] and 0 <= x + directions["bottom-left"][1] < data.shape[1]):
        return False
    letters.append(data[y + directions["bottom-left"][0]][x + directions["bottom-left"][1]])
    if not (0 <= y + directions["bottom-right"][0] < data.shape[0] and 0 <= x + directions["bottom-right"][1] < data.shape[1]):
        return False
    letters.append(data[y + directions["bottom-right"][0]][x + directions["bottom-right"][1]])
    if letters.count('M') == 2 and letters.count('S') == 2:
        if not ((letters[0] == 'M' and letters[3] == 'M') or (letters[1] == 'M' and letters[2] == 'M')):
            return True
    return False


#Iterate through data, once you hit a X check for xmas in every direction
count = 0
x_count = 0
for y in range(height):
    for x in range(width):
        #Part 1
        if data[y][x] == 'X':
            count += check_directions(y, x, directions, data)
        #Part 2
        if data[y][x] == 'A':
            if check_x(y, x, data):
                x_count += 1

print(count)
print(x_count)
