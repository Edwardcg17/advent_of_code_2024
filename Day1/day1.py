import numpy as np
from collections import defaultdict

#Part 1
data = np.loadtxt("Day1\day1_input.txt")
col1 = np.sort(data[:,0])
col2 = np.sort(data[:,1])

answer = np.sum(np.abs(col1 - col2))
print(answer)


#Part 2
similarity = defaultdict(float)
total = 0
for element in col1:
    if element not in similarity.keys():
        similarity[element] = np.count_nonzero(col2 == element)
    total += element * similarity[element]
print(total)
