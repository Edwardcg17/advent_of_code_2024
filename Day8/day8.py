import numpy as np
from itertools import combinations

data = []
with open(r"Day8\day8_input.txt", 'r') as file:
    for line in file:
        row = list(line.strip())  
        data.append(row)

data = np.array(data)

#Get all unique elements, delete '.' which is at index 0
antennas = np.delete(np.unique(data), 0)
antinodes = set()

#For each antenna look for matching ones, calculate antinodes
for antenna in antennas:
    indices = np.where(data == antenna)
    coordinates = list(zip(indices[0], indices[1]))
    pairings = list(combinations(coordinates, 2))
    
    #For each pair of matching antennas calculate antinode locations
    for pair in pairings:
        coord1 = np.array(pair[0])
        coord2 = np.array(pair[1])
        difference = coord1 - coord2

        in_bounds = True
        i = 0
        while in_bounds:
            antinode1 = coord1 + difference * i
            if (0 <= antinode1[0] < data.shape[0] and 0 <= antinode1[1] < data.shape[1]):
                antinodes.add(tuple(antinode1))
                i += 1
            else:
                in_bounds = False
            
        in_bounds = True
        i = 0
        while in_bounds:
            antinode2 = coord2 - difference * i
            if (0 <= antinode2[0] < data.shape[0] and 0 <= antinode2[1] < data.shape[1]):
                antinodes.add(tuple(antinode2))
                i += 1
            else:
                in_bounds = False

print(len(antinodes))


