# second puzzle

def part_one(instructions):
    x = 0
    y = 0
    for i in instructions:
        if i[0] == 'forward':
            x += int(i[1])
        elif i[0] == 'down':
            y += int(i[1])
        elif i[0] == 'up':
            y -= int(i[1])
    return x * y

def part_two(instructions):
    x = 0
    y = 0
    aim = 0
    for i in instructions:
        if i[0] == 'forward':
            x += int(i[1])
            y += aim * int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'up':
            aim -= int(i[1])
    return x * y

with open('input.txt', 'r') as file:
    puzzle_input = [line.strip().split(" ") for line in file]

print(part_one(puzzle_input))
print(part_two(puzzle_input))