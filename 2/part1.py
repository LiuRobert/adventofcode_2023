import sys, os, re
sys.path.append(os.path.abspath('.'))
from util import read_input_lines, read_test_lines

# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

def get_game_id(line) -> int:
    str_id = re.findall(r"(?<=Game\s)\d+", line)[0]
    return int(str_id)

def get_max_cubes(color: str, line) -> int:
    instances = re.findall(r"\d+(?=\s" + color + ")", line)
    instances = [int(i) for i in instances]
    instances.sort(reverse=True)
    return instances[0]

result = 0
lines = read_input_lines("2")

for line in lines:
    if get_max_cubes("red", line) <= 12 and get_max_cubes("green", line) <= 13 and get_max_cubes("blue", line) <= 14:
        result += get_game_id(line)

print(result)
