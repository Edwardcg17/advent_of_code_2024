from collections import defaultdict

with open("Day5/day5_input.txt", 'r') as file:
    lines = file.readlines()

#-----------------------------------------------------Parse Data---------------------------------------#
rules = []
updates = []
appending_rules = True

for line in lines:
    stripped_line = line.strip()

    if stripped_line == "":
        appending_rules = False
        continue
    
    if appending_rules:
        rules.append(stripped_line) #Turn into list of ints later, after | is removed
    else:
        updates.append([int(element) for element in stripped_line.split(",")]) #Turning into list of ints

rules_dict = defaultdict(list) #Dictionary mapping page to all pages that must come after
for rule in rules:
    pages = rule.split("|")
    rules_dict[int(pages[0])].append(int(pages[1]))

#-----------------------------------------------------Part 1----------------------------------------------#
correct_updates = []
incorrect_updates = []
for line in updates:
    correctly_ordered = True
    for number in line:
        pages_after = rules_dict[number]
        for later_page in pages_after:
            if (later_page in line) and not (line.index(number) < line.index(later_page)):
                correctly_ordered = False
                break
        if not correctly_ordered:
            break
    if correctly_ordered: #If all numbers were looped through and are in the correct order
        correct_updates.append(line)
    else:
        incorrect_updates.append(line)

total = 0
for line in correct_updates:
    total += line[(len(line)// 2)]
print(f"Part 1 Answer: {total}")

#-----------------------------------------------------Part 2----------------------------------------------#
re_ordered = []
for line in incorrect_updates:
    print(line)
    re_ordered_line = line.copy()
    for number in line:
        left = []
        right = []
        pages_after = rules_dict[number]
        for number2 in re_ordered_line:
            if number2 in pages_after:
                right.append(number2)
            else:
                left.append(number2)
        re_ordered_line = left + right
    re_ordered.append(re_ordered_line)

re_order_total = 0
for line in re_ordered:
    re_order_total += line[len(line) // 2]
print(f"Part 2 Answer: {re_order_total}")

