import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def is_int(num): # Checks if an item in the list is a number
    try:
        int(num)
        return True
    except ValueError:
        return False

def file_sum_check(lst): # Takes final list and does check count
    counter = 0
    for i in range(len(lst)):
        if is_int(lst[i]):
            counter += i * int(lst[i])
    return counter

def disk_list(string, part): # Turns input into initial list
    list_unsorted = []
    for id, file_space in enumerate(re.findall(r'(\d)(\d?)', string)): # id, file length, space length
        file, space = file_space
        if space == '': space = '0'
        if part == 1: # Part 1
            list_unsorted.extend([str(id)] * int(file)) # Makes 1 list
            list_unsorted.extend(['.'] * int(space))
        elif part == 2: # Part 2
            list_unsorted.append([str(id)] * int(file)) # Makes list of lists
            if space != '0': # Edge case I didn't like
                list_unsorted.append(['.'] * int(space))
    return list_unsorted

def flatten(xss): # Turn list of lists into 1 list for check sum
    return [x for xs in xss for x in xs]

def part1(puzzle):
    list_unsorted = disk_list(puzzle, 1)
    j = len(list_unsorted) - 1 # For heading backwards through the file
    for i in range(len(list_unsorted)): # Iterates through file
        if list_unsorted[i] == '.':
            if j <= i:
                break
            while True:
                if is_int(list_unsorted[j]): # If file number
                    list_unsorted[i], list_unsorted[j] = list_unsorted[j], list_unsorted[i] # Swaps space and number
                    break
                j -= 1
    return file_sum_check(list_unsorted)

def part2(puzzle):
    list_unsorted = disk_list(puzzle, 2)
    list_sorting = list_unsorted.copy()
    for i in range(len(list_unsorted))[::-1]: # Iterates backwards for each file
        if list_unsorted[i][0] == '.': # Skips spaces
            continue
        for j in range(len(list_sorting)): # Iterates forwards for each space
            if list_unsorted[i] == list_sorting[j]: # Breaks if nowhere to place file
                break
            if list_sorting[j][0] != '.': # Skips files
                continue
            elif len(list_unsorted[i]) == len(list_sorting[j]): # Switch equally sized files with spaces
                list_sorting[list_sorting.index(list_unsorted[i])] = ['.'] * len(list_sorting[j])
                list_sorting[j] = list_unsorted[i]
                break
            elif len(list_unsorted[i]) <= len(list_sorting[j]): # Switch (smaller files + smaller space) with spaces
                list_sorting[list_sorting.index(list_unsorted[i])] = ['.'] * len(list_unsorted[i])
                list_sorting[j:j+1] = (list_unsorted[i], ['.'] * (len(list_sorting[j])-len(list_unsorted[i])))
                break
    return file_sum_check(flatten(list_sorting))

print(f'Part 1: {part1(puzzle_input)}')
print(f'Part 2: {part2(puzzle_input)}')