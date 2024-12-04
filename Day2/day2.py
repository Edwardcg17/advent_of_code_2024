import numpy as np

#Part 1
def is_increasing_safely(lst):
    return all((lst[i] < lst[i + 1]) and (1 <= lst[i + 1] - lst[i] <= 3) for i in range(len(lst) - 1))

def is_decreasing_safely(lst):
    return all((lst[i] > lst[i + 1]) and (1 <= lst[i] - lst[i + 1] <= 3) for i in range(len(lst) - 1))

def is_safe(lst):
    return is_increasing_safely(lst) or is_decreasing_safely(lst)

data = []
with open(r"Day2\day2_input.txt", 'r') as file:
    for line in file:
        row = line.split()  
        row = [int(x) for x in row]
        data.append(row)

safe_count = 0
for row in data:
    if is_safe(row):
        safe_count += 1
print(safe_count)

#Part 2
damp_safe_count = 0
for row in data:
    if is_safe(row):
        damp_safe_count += 1
    else:
        for i, n in enumerate(row):
            removed_row = row[:i] + row[i + 1:]
            if is_safe(removed_row):
                damp_safe_count += 1
                break
print(damp_safe_count)