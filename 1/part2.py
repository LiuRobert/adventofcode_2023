import sys, os, re
sys.path.append(os.path.abspath('.'))
from util import read_input_lines, read_test_lines

# Does not work!

translate_table = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def to_num(s: str) -> int:
    if re.match("[1-9]", s):
        return s
    return translate_table[s]

result = 0
lines = read_input_lines("1")
for line in lines:
    finds = re.findall("[1-9]|one|two|three|four|five|six|seven|eight|nine", line)
    first = finds[0]
    last = finds[-1]
    print(first + last)
    result += int(to_num(first) + to_num(last))

# print(result)
