import os

def read_input_lines(folder):
    with open(os.path.join(folder, "input.txt"), "r") as f:
        return f.read().splitlines()
    
def read_test_lines(folder):
    with open(os.path.join(folder, "test.txt"), "r") as f:
        return f.read().splitlines()