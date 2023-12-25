from tqdm import tqdm
directions = {'R':(1, 0), 'D':(0, 1), 'L':(-1, 0), 'U':(0, -1)}

def count_area(instructions):
    num = 0
    curr = (0, 0)
    points: list[tuple[int, int]] = []
    for [direction, steps, _] in instructions:
        points.append(curr)
        num += steps
        dir_letter = directions[direction]
        curr = (curr[0] + dir_letter[0] * steps, curr[1] + dir_letter[1] * steps)
    
    area = 0
    for i in range(len(points)):
        area += points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1])
        
    return ((abs(area) // 2) - num // 2 + 1) + num

def part1(input):
    instructions = [[i[0], int(i[1]), i[2][2:-1]] for i in [x.split() for x in input.splitlines()]]

    return count_area(instructions)
    
    
def part2(input):
    instructions = [[i[0], int(i[1]), i[2][2:-1]] for i in [x.split() for x in input.splitlines()]]
    
    for i in instructions:
        i[0] = list(directions)[int(i[2][-1])]
        i[1] = int(i[2][:-1], 16)

    return count_area(instructions)