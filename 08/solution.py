def create_network(input):
    network = dict()
    steps, lines = input.split("\n\n")
    for line in lines.splitlines():
        key, value = line.split(" = ")
        value = value[1:-1].split(", ")
        network[key] = value
    return steps, network

def part1(input):
    steps, network = create_network(input)
        
    count = 0
    c = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        count += 1
        
        dir = 0 if steps[c] == 'L' else 1
        curr = network.get(curr)[dir]
        
        c += 1
        if c >= len(steps):
            c = 0
    
    return count
    
def part2(input):
    steps, network = create_network(input)
    
    starts = [x for x in network.keys() if x[-1] == 'A']
    
    record = 0
    count = 0
    c = 0
    curr = starts
    while len([x for x in curr if x[-1] == 'Z']) != len(starts):
        test = len([x for x in curr if x[-1] == 'Z'])
        if test > record:
            record = test
            print(f"Record of simultaneous end points: {record}")

        dir = 0 if steps[c] == 'L' else 1
        curr = [network.get(i)[dir] for i in curr]
        
        count += 1
        c += 1
        if c >= len(steps):
            c = 0
    
    return count