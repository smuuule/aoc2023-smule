def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(lst: list) -> int:
    curr = 1
    for i in lst:
        curr = (curr * i) // gcd(curr, i)
    
    return curr  
    
def create_network(input):
    network = dict()
    steps, _, *lines = input.splitlines()
    for line in lines:
        key, value = line.split(" = ")
        value = value[1:-1].split(", ")
        network[key] = value
    return steps, network

def network_steps(network, steps, start, end):
    count = 0
    c = 0
    curr = start
    while curr not in end:
        count += 1
        
        dir = 0 if steps[c] == 'L' else 1
        curr = network.get(curr)[dir]
        
        c += 1
        if c >= len(steps):
            c = 0
    
    return count

def part1(input):
    steps, network = create_network(input)
        
    return network_steps(network, steps, 'AAA', ['ZZZ'])
    
def part2(input):
    steps, network = create_network(input)
    
    starts = [x for x in network.keys() if x[-1] == 'A']
    ends = [x for x in network.keys() if x[-1] == 'Z']
    step_amounts = []
    
    for start in starts:
        step_amounts.append(network_steps(network, steps, start, ends))
    
    return lcm(step_amounts)