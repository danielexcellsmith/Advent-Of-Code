import numpy as np
import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1part2(puzzle, num): # I love regex
    counter = 0
    for x1, y1, x2, y2, x, y in re.findall(
            r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', puzzle):
        A = np.array([[int(x1), int(x2)], [int(y1), int(y2)]]) # Simultaneous Equations in Matrix
        B = np.array([num + int(x), num + int(y)]) # Prize Value
        C = np.linalg.solve(A, B) # Solves
        if round(C[0], 3).is_integer() and round(C[1], 3).is_integer(): # Only the integer solutions
            counter += C[0] * 3 + C[1]
    return int(counter)

print(f'Part 1: {part1part2(puzzle_input, 0)}')
print(f'Part 2: {part1part2(puzzle_input, 10000000000000)}')
