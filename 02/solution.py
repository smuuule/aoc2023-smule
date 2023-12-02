def getCounts(game) -> list[list[int]]:
    n, cubes = game[5:].split(': ',)
    counts = [[0]*3 for _ in range(len(cubes.split('; ')))]
    i = 0
    for grab in cubes.split('; '):
        for color in grab.split(', '):
            match color.split(' ')[1]:
                case 'red':
                    counts[i][0] += int(color.split(' ')[0])
                case 'green':
                    counts[i][1] += int(color.split(' ')[0])
                case 'blue':
                    counts[i][2] += int(color.split(' ')[0])
        
        i += 1
    
    return counts

def possibleGame(game) -> bool:
    possible = [12,13,14] # RGB
    counts = getCounts(game)

    for i, max in enumerate(possible):
        for grab in counts:
            if grab[i] > max:
                return False
    
    return True

def maxCubes(game) -> list[int]:
    counts = getCounts(game)
    mins = counts[0]

    for grab in counts:
        for i, count in enumerate(grab):
            if count > mins[i]:
                mins[i] = count

    return mins

def part1(input):
    count = 0
    for i, game in enumerate(input.splitlines()):
        if possibleGame(game):
            count += i+1
    
    return count
    
def part2(input):
    powers = []

    for i, game in enumerate(input.splitlines()):
        cubes = maxCubes(game)
        power = 1
        for i in cubes:
            power *= i

        powers.append(power)
        
    
    return sum(powers)