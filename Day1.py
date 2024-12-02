import os

os.chdir("/Users/danielexcellsmith/Advent of Code 2024 - Python/")
with open("Day1.txt", 'r') as f:
    puzzle_input = f.read()

def part1(puzzle):
    left_list = []
    right_list = []
    for line in puzzle.split('\n'):
        line_list = line.split('   ')
        left_list.append(int(line_list[0]))
        right_list.append(int(line_list[1]))
    left_list.sort()
    right_list.sort()
    counter = 0
    for i in range(len(left_list)):
        counter += abs(left_list[i] - right_list[i])
    return counter

def part2(puzzle):
    left_list = []
    right_list = []
    for line in puzzle.split('\n'):
        line_list = line.split('   ')
        left_list.append(int(line_list[0]))
        right_list.append(int(line_list[1]))
    counter = 0
    for num in left_list:
        counter += num * right_list.count(num)
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')