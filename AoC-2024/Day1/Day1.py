with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def create_lists(puzzle):
    left_list = []
    right_list = []
    for line in puzzle.split('\n'):
        line_list = line.split('   ')
        left_list.append(int(line_list[0]))
        right_list.append(int(line_list[1]))
    return left_list, right_list

def part1(puzzle):
    left_list, right_list = create_lists(puzzle)
    left_list.sort()
    right_list.sort()
    counter = 0
    for i in range(len(left_list)):
        counter += abs(left_list[i] - right_list[i])
    return counter

def part2(puzzle):
    left_list, right_list = create_lists(puzzle)
    counter = 0
    for num in left_list:
        counter += num * right_list.count(num)
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')