import re

with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def update_check(rules, pages):
    for x, y in re.findall(r'(\d{2})\|(\d{2})', rules): # Regex on rules
        if x not in pages or y not in pages: # Skip irrelevant rules
            continue
        if pages.index(x) > pages.index(y): # Any broken rule => False
            return False
    return True # No broken rules

def update_change(rules, pages):
    for i in range(len(pages) - 1):
        for x, y in re.findall(r'(\d{2})\|(\d{2})', rules): # Inefficient but works
            if pages[i] == y and pages[i + 1] == x: # Checks each page against next page
                pages[i], pages[i + 1] = x, y # Flips pages if necessary
    return pages

def part1(puzzle):
    rules, updates = puzzle.split('\n\n')
    counter = 0
    wrong_orders = []
    for line in updates.split('\n'):
        pages = line.split(',')
        if update_check(rules, pages):
            counter += int(pages[len(pages) // 2])
        else:
            wrong_orders.append(pages) # Used for Part 2
    return counter, rules, wrong_orders

def part2(puzzle):
    rules = puzzle.split('\n\n')[0]
    updates = part1(puzzle)[2]
    counter = 0
    for pages in updates: # For each incorrect update
        new_order = pages.copy()
        while not update_check(rules, new_order): # Until each update is in the correct order
            new_order = update_change(rules, new_order)
        counter += int(new_order[len(new_order) // 2])
    return counter

print(f'Part 1: {part1(puzzle_input)[0]}')
print(f'Part 2: {part2(puzzle_input)}')
