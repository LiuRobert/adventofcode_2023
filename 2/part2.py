import sys, os, re
sys.path.append(os.path.abspath('.'))
from util import read_input_lines, read_test_lines

def get_max_cubes(color: str, line) -> int:
    instances = re.findall(r"\d+(?=\s" + color + ")", line)
    instances = [int(i) for i in instances]
    instances.sort(reverse=True)
    return instances[0]

result = 0
lines = read_input_lines("2")

for line in lines:
    red = get_max_cubes("red", line)
    green = get_max_cubes("green", line)
    blue = get_max_cubes("blue", line)
    result += red * green * blue

print(result)
