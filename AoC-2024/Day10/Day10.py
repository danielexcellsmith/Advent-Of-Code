with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1part2(puzzle, part):
    directions = [(0,1),(0,-1),(1,0),(-1,0)] # Right Left Down Up
    puzzle_list = puzzle.split('\n')
    counter = 0
    for i, line in enumerate(puzzle_list):
        for j, char in enumerate(line):
            if char != '0': # Only start at '0'
                continue
            else:
                old_locations = [[i,j]]
                for num in range(9): # Going from 0 to 9
                    new_locations = []
                    for x in old_locations: # Keeping track of current path locations
                        for y in range(4): # Iterate through directions
                            if x[0] + directions[y][0] < 0 or x[1] + directions[y][1] < 0 or x[0] + directions[y][0] >= len(puzzle_list) or x[1] + directions[y][1] >= len(line):
                                continue
                            location = [x[0] + directions[y][0], x[1] + directions[y][1]] # Test new location
                            if int(puzzle_list[location[0]][location[1]]) == num + 1: # If new location is one larger
                                if part == 1 and location not in new_locations: # Part 1
                                    new_locations.append(location)
                                elif part == 2: # Part 2 (Unique paths)
                                    new_locations.append(location)
                    old_locations = new_locations
                counter += len(new_locations) # Adds number of final locations
    return counter

print(f'Part 1: {part1part2(puzzle_input, 1)}')
print(f'Part 2: {part1part2(puzzle_input, 2)}')