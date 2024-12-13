import numpy as np
import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1part2(puzzle, num): # I love regex
    counter = 0
    for a1, a2, b1, b2, x, y in re.findall(
            r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', puzzle):
        A = np.array([[int(a1), int(b1)], [int(a2), int(b2)]])
        B = np.array([num + int(x), num + int(y)])
        C = np.linalg.solve(A, B)
        if round(C[0], 3).is_integer() and round(C[1], 3).is_integer(): # Only the integer solutions
            counter += C[0] * 3 + C[1]
    return int(counter)

print(f'Part 1: {part1part2(puzzle_input, 0)}')
print(f'Part 2: {part1part2(puzzle_input, 10000000000000)}')