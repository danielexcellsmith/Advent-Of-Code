import math
import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def program(A, B, C, instructions):
    output = []
    operands = {'0': 0, '1': 1, '2': 2, '3': 3, '4': A, '5': B, '6': C, '7': 7}
    instruction_list = re.findall(r'\d+', instructions)
    i = 0
    while True:
        try: # End program if reaches the end of the list
            instruction_list[i + 1]
        except:
            break
        opcode = instruction_list[i]
        operand = instruction_list[i + 1]
        if opcode == '0': # Separate instruction for each code
            A = math.trunc(A / pow(2, operands[operand]))
            operands['4'] = A
        elif opcode == '1':
            B = B ^ int(operand)
            operands['5'] = B
        elif opcode == '2':
            B = operands[operand] % 8
            operands['5'] = B
        elif opcode == '3':
            if A != 0:
                i = int(operand)
            else:
                i += 2
            continue
        elif opcode == '4':
            B = B ^ C
            operands['5'] = B
        elif opcode == '5':
            output.append(str(operands[operand] % 8))
        elif opcode == '6':
            B = math.trunc(A / pow(2, operands[operand]))
            operands['5'] = B
        elif opcode == '7':
            C = math.trunc(A / pow(2, operands[operand]))
            operands['6'] = C
        i += 2
    return output

def part1(puzzle):
    abc, instructions = puzzle.split('\n\n')
    A, B, C = re.findall(r'\d+', abc)
    A, B, C = int(A), int(B), int(C) # Initial values
    return program(A, B, C, instructions)

def part2(puzzle):
    i = 1
    abc, instructions = puzzle.split('\n\n')
    instructions_list = re.findall(r'\d+', instructions)
    output = program(i, 0, 0, instructions)
    while len(output) < len(instructions_list): # Makes output long enough
        i *= 8
        output = program(i, 0, 0, instructions)
    while output != instructions_list: # Until output is correct
        for j in range(16)[::-1]: # Iterates backwards through output
            while output[j] != instructions_list[j]:
                i += pow(8,j)
                output = program(i, 0, 0, instructions)
    return i

print(f'Part 1: {','.join(part1(puzzle_input))}')
print(f'Part 2: {part2(puzzle_input)}')