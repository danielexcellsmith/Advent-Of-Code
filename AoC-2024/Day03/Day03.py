import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1(puzzle):
    counter = 0
    for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle): # all multiplication instructions
        counter += int(x) * int(y)
    return counter

def part2(puzzle):
    counter = 0
    for line in puzzle.split("do()"): # each line is of the form "... don't() ..."
        counter += part1(line.split("don't()")[0]) # take part before the don't()
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')
