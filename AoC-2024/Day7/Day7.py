with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def format_base(n, b): # Formats number n to base b
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums))

def part1part2(puzzle, base):
    counter = 0
    for line in puzzle.split('\n'):
        result = int(line.split(': ')[0]) # Required answer
        equation = line.split(': ')[1].split(' ') # Equation list
        perms = pow(base, len(equation) - 1) # Number of permutations of operators
        for i in range(perms):
            test_result = int(equation[0]) # Starts at first number
            i_format = format_base(i,base).zfill(len(equation)-1) # Turns perm to binary/trinary
            for j in range(len(equation) - 1):
                if i_format[j] == '0':
                    test_result += int(equation[j + 1])
                elif i_format[j] == '1':
                    test_result *= int(equation[j + 1])
                else: # Only needed for part 2
                    test_result = int(str(test_result) + equation[j+1])
            if test_result == result:
                counter += result
                break
    return counter

print(f'Part 1: {part1part2(puzzle_input, 2)}')
print(f'Part 2: {part1part2(puzzle_input, 3)}')