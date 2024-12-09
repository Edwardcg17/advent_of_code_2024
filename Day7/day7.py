import re

data = []
with open(r"Day7\day7_input.txt", 'r') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        data.append([int(num) for num in numbers])

def can_concate(num1, num2):
    if len(str(abs(num2))) > len(str(abs(num1))):
        return False
    
    modder = 1
    for i in range(len(str(abs(num2)))):
        modder *= 10

    if (num1 % modder) == num2:
        return True
    
def can_calibrate(data: list[int]) -> bool:
    if len(data) == 2:
        if data[0] == data[1]:
            return True
        else:
            return False

    add_list = [data[0] - data[-1]] + data[1:-1]
    mul_list = [data[0] / data[-1]] + data[1:-1]
    
    if (can_concate(data[0], data[-1])):
        modder = 1
        for i in range(len(str(abs(data[-1])))):
            modder *= 10
        concate_list = [data[0] // modder] + data[1: -1]
        return can_calibrate(add_list) or can_calibrate(mul_list) or can_calibrate(concate_list)

    else:
        return can_calibrate(add_list) or can_calibrate(mul_list)

total = 0
for line in data:
    if can_calibrate(line):
        total += line[0]
print(total)

# test = [3267, 81, 40, 27]
# can_calibrate(test)