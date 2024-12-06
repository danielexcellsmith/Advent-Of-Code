with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def start_position(puzzle_list): # Returns [59,70]
    for i in range(len(puzzle_list)):
        for j in range(len(puzzle_list[0])):
            if puzzle_list[i][j] == '^':
                return [i,j]

def part1(puzzle): # Don't look at me, I'm hideous
    puzzle_list = puzzle.split('\n')
    direction_list = ['^', '>', 'v', '<', '^']
    current_position = [[59,70], '^']
    directions = {'^': [-1,0], '>': [0,1], 'v': [1,0], '<': [0,-1]}
    locations_visited = [current_position[0]]
    locations_and_directions = current_position
    while True: # Seriously, this code sucks
        new_position = [current_position[0][i] + directions[current_position[1]][i] for i in range(2)]
        new_letter = current_position[1]
        if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(puzzle_list) or new_position[1] >= len(puzzle_list[0]):
            break # Ends if leaving the grid
        if puzzle_list[new_position[0]][new_position[1]] == '#': # Hoping I can do better for Day 7
            new_letter = direction_list[direction_list.index(new_letter) + 1]
            new_position = [current_position[0][i] + directions[new_letter][i] for i in range(2)]
            if puzzle_list[new_position[0]][new_position[1]] == '#': # That stupid U-Turn case
                new_letter = direction_list[direction_list.index(new_letter) + 1]
                new_position = [current_position[0][i] + directions[new_letter][i] for i in range(2)]
        current_position = [new_position, new_letter]
        if new_position not in locations_visited: # Oh look, an if statement, how fun and different...
            locations_visited.append(new_position)
        if current_position in locations_and_directions:
            return len(locations_visited), True, locations_visited # True if a loop is created
        else:
            locations_and_directions.append(current_position) # Adds current position and direction if new
    return len(locations_visited), False, locations_visited

def part2(puzzle):
    puzzle_list = puzzle.split('\n')
    counter = 0
    locations = part1(puzzle)[2]
    locations.pop(0)
    for loc in locations: # Just needs to iterate through the 5000+ locations in the first path
        puzzle_matrix = [list(puzzle_list[i]) for i in range(len(puzzle_list))]
        puzzle_matrix[loc[0]][loc[1]] = '#' # Changes the '.' to a '#'
        new_puzzle_list = [''.join(puzzle_matrix[i]) for i in range(len(puzzle_list))]
        new_puzzle = '\n'.join(new_puzzle_list) # Makes new puzzle grid to call part1 for
        if part1(new_puzzle)[1]: # If loop created
            counter += 1
            print(counter, locations.index(loc)) # Just so I can see my code is doing something for 20 minutes
    return counter

print(f'Part 1: {part1(puzzle_input)[0]}')
print(f'Part 2: {part2(puzzle_input)}')