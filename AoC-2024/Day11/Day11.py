with open("input.txt", 'r') as f:
    puzzle_input = f.read()

def part1part2(puzzle, blinks):
    stones = []
    stones_number = []
    for stone in puzzle.split(' '):
        stones.append(int(stone))
        stones_number.append(1)
    for _ in range(blinks):
        new_stones = [] # Unique stones
        new_stones_number = [] # List of number of occurrences of each stone
        for stone in stones:
            num = stones_number[stones.index(stone)]
            if stone == 0:
                new_stone = 1
                if new_stone not in new_stones:
                    new_stones.append(new_stone) # Add to list if unique
                    new_stones_number.append(num) # Add number to list
                else:
                    new_stones_number[new_stones.index(new_stone)] += num # Add number to existing occurrences
            elif len(str(stone)) % 2 == 0:
                new_stone = int(str(stone)[:len(str(stone))//2])
                if new_stone not in new_stones:
                    new_stones.append(new_stone)
                    new_stones_number.append(num)
                else:
                    new_stones_number[new_stones.index(new_stone)] += num
                new_stone = int(str(stone)[len(str(stone))//2:])
                if new_stone not in new_stones:
                    new_stones.append(new_stone)
                    new_stones_number.append(num)
                else:
                    new_stones_number[new_stones.index(new_stone)] += num
            else:
                new_stone = stone * 2024
                if new_stone not in new_stones:
                    new_stones.append(new_stone)
                    new_stones_number.append(num)
                else:
                    new_stones_number[new_stones.index(stone)] += num
        stones = new_stones
        stones_number = new_stones_number
    return sum(stones_number)

print(f'Part 1: {part1part2(puzzle_input, 25)}')
print(f'Part 2: {part1part2(puzzle_input, 75)}')