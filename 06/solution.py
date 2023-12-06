def part1(input):

    time, distance = [j.split() for j in [i.split(": ")[1] for i in input.splitlines()]]
    time = [int(i) for i in time]
    distance = [int(i) for i in distance]

    waysToWin = []
    race = 0
    while race < len(time):

        raceDistance = []
        for i in range(0, time[race]):
            raceDistance.append(i * (time[race] - i))

        raceDistance = list(filter(lambda i: i > distance[race], raceDistance))
        waysToWin.append(len(raceDistance))

        race += 1
    
    result = 1
    for i in waysToWin:
        result *= i

    return result
    
def part2(input):

    time, distance = [int(i.split(":")[1].replace(" ", "")) for i in input.splitlines()]
    print(time, distance)

    waysToWin = []
    raceDistance = []
    for i in range(0, time):
        raceDistance.append(i * (time - i))

    raceDistance = list(filter(lambda i: i > distance, raceDistance))
    waysToWin.append(len(raceDistance))
    
    result = 1
    for i in waysToWin:
        result *= i

    return result