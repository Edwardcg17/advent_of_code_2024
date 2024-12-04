from collections import deque

MAXLENGTH = 8 #Max length of characters after mul( (3 number, 1 comma, 3 number, 1 closing parenthesis)

with open(r"Day3\day3_input.txt", 'r') as file:
    content = file.read()

total = 0
prev_four = deque(maxlen=4)
do_dont_checker = deque(maxlen=7)
enabled = True

for i, c in enumerate(content):
    prev_four.append(c)
    do_dont_checker.append(c)

    #Check if you are enabled
    if "don't()" in ''.join(do_dont_checker):
        enabled = False
    if "do()" in ''.join(do_dont_checker):
        enabled = True

    if enabled:
        #if last 4 characters form mul, check for number, number) 
        if ''.join(prev_four) == "mul(":
            next_chars = content[i + 1: i + MAXLENGTH + 1]

            index = next_chars.find(')')
            if index == -1: #If ) is not found in the substring
                continue
            else:
                substring = next_chars[: index]

                #This is now everything inside the parenthesis
                if not (substring.count(',') == 1):
                    continue
                else:
                    #Check if after splitting, everything is numbers and numbers are valid
                    split_string = substring.split(',')
                    num1 = split_string[0]
                    num2 = split_string[1]
                    if not ((num1.isdigit() and num2.isdigit()) and (len(num1) <= 3 and len(num2) <= 3)):
                        continue
                    else:
                        total += int(num1) * int(num2)

print(total)
        
