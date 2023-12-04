# advent of code day 1

import re

input = open("input.txt", "r")
lines = input.readlines()

text_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum = 0

for line in lines:
    numbers = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
    if not numbers[0].isdigit():
       numbers[0] = text_to_digit[numbers[0]]
    if not numbers[-1].isdigit():
        numbers[-1] = text_to_digit[numbers[-1]]
    twoDigits = int(str(numbers[0]) + str(numbers[-1]))
    sum = sum + twoDigits
    
print("sum: ", sum)
input.close()


