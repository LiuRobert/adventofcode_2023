import sys, os, re
sys.path.append(os.path.abspath('.'))
from util import read_input_lines

result = 0
lines = read_input_lines("1")
for line in lines:
    numbers = re.sub(r"[A-z]", "", line)
    result += int(numbers[0] + numbers[-1])
    
print(result)