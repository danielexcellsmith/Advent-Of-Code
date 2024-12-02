with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def safe_check(line): # checks if a line is safe
    safe = True
    line_list = line.split(' ')
    if 4 > int(line_list[1]) - int(line_list[0]) > 0: # does the list need to be all ascending?
        for i in range(len(line_list) - 1):
            if 3 < int(line_list[i + 1]) - int(line_list[i]) or int(line_list[i + 1]) - int(line_list[i]) < 1:
                safe = False
    elif -4 < int(line_list[1]) - int(line_list[0]) < 0:
        for i in range(len(line_list) - 1):
            if -3 > int(line_list[i + 1]) - int(line_list[i]) or int(line_list[i + 1]) - int(line_list[i]) > -1:
                safe = False
    else:
        safe = False
    return safe

def part1(puzzle):
    counter = 0
    for line in puzzle.split('\n'):
        if safe_check(line):
            counter += 1
    return counter

def part2(puzzle):
    counter = 0
    for line in puzzle.split('\n'):
        if safe_check(line): # Part 1
            counter += 1
        else:
            for i in range(len(line.split(' '))):
                line_list = line.split(' ')
                line_list.pop(i) # takes one item out of the list at a time
                new_line = ' '.join(line_list) # joins the line
                if safe_check(new_line): # uses same checking function but with shorter line
                    counter += 1
                    break
    return counter

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')