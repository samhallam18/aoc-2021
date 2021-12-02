# first puzzle
def part_one(depths):
    answer = 0
    previous = depths[0]
    for i in range(1, len(depths)):
        current = depths[i]
        if current > previous:
            answer += 1
        previous = current
    return answer

def part_two(depths):
    answer = 0
    previous = 0
    for i in range(0, 2):
        previous += depths[i]
    for j in range(1, len(depths) - 3):
        current = depths[j] + depths[j+1] + depths[j+2]
        if current > previous:
            answer += 1
        previous = current
    return answer


with open ('input.txt', 'r') as file:
    puzzle_input = [line.strip() for line in file]

puzzle_input = [int(i) for i in puzzle_input]

print(part_one(puzzle_input))
print(part_two(puzzle_input))