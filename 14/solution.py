def tilt_north(platform):
    for i, row in enumerate(platform):
        for j, pos in enumerate(row):
            if pos == 'O':
                y = i
                while y > 0 and platform[y-1][j] == '.':
                    platform[y][j] = '.'
                    platform[y-1][j] = 'O'
                    y -= 1
    return platform

def rotate_clockwise(platform):
    return [list(i) for i in zip(*reversed(platform))]

def calc_load(platform):
    load = 0
    height = len(platform)
    for i, row in enumerate(platform):
        num = row.count('O')
        load += num*(height-i)
        
    return load

def cycle_load(platform, num):
    seen = {}
    for i in range(1, num):
        for j in range(4):
            platform = rotate_clockwise(tilt_north(platform))
    
        if str(platform) not in seen.keys():
            seen[str(platform)] = (i, calc_load(platform))
            continue
        else:
            platformindex = seen[str(platform)][0]
            cycleindex = platformindex + (num - platformindex) % (i - platformindex)
            return [i[1] for i in seen.values() if i[0] == cycleindex][0]
            
            return -1
    
    return -1

def part1(input):
    platform = [list(i) for i in input.splitlines()]
    return calc_load(tilt_north(platform))
    
def part2(input):
    platform = [list(i) for i in input.splitlines()]
    return cycle_load(platform, 1000000000)