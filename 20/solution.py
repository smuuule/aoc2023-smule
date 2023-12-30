class Module:
    def __init__(self, name, type, dest) -> None:
        self.name = name
        self.type = type
        self.dest = dest
        self.prev = 0 if type == 'ff' else {}
    
    def __repr__(self) -> str:
        return self.name + "{" + f"{self.type=}, {self.dest=}, {self.prev}"
    
    def send(self):
        if self.type == 'bc':
            return [(i, 0) for i in self.dest]
        elif self.type == 'cj':
            return
        elif self.type == 'ff':
            return

class Graph:
    def __init__(self, input) -> None:
        self.graph = {}
        for l, r in [line.split(' -> ') for line in input.splitlines()]:
            name = l if l.isalpha() else l[1:]
            if l[0] == '%':
                self.graph[name] = Module(name, 'ff', r.split(', '))
            elif l[0] == '&':
                self.graph[name] = Module(name, 'cj', r.split(', '))
            else:
                self.graph[name] = Module(name, 'bc', r.split(', '))

        for name, module in self.graph.items():
            for dest in module.dest:
                if dest in self.graph and self.graph[dest].type == 'cj':
                    self.graph[dest].prev[name] = 0
        
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(lst: list) -> int:
    curr = 1
    for i in lst:
        curr = (curr * i) // gcd(curr, i)
    
    return curr

def part1(input):

    g = Graph(input)

    lo, hi = 0, 0
    for _ in range(1000):
        lo += 1
        q = [('bc', i, 0) for i in g.graph['broadcaster'].dest]

        while q:
            root, dest, state = q.pop(0)
            if state == 0:
                lo += 1
            else:
                hi += 1

            if dest not in g.graph:
                continue

            module = g.graph[dest]

            if module.type == 'ff':
                if state == 0:
                    module.prev = 1 if module.prev == 0 else 0
                    newstate = 1 if module.prev == 1 else 0
                    for i in module.dest:
                        q.append((module.name, i, newstate))
            else:
                module.prev[root] = state
                newstate = 0 if all(x == 1 for x in module.prev.values()) else 1
                for i in module.dest:
                    q.append((module.name, i, newstate))
                
    return lo * hi
    
def part2(input):
    
    g = Graph(input)

    rx = [i for i, module in g.graph.items() if 'rx' in module.dest][0]
    counts = {i: 0 for i, module in g.graph.items() if rx in module.dest}
    cycle_lengths = {}

    count = 0
    while True:
        count += 1
        q = [('bc', i, 0) for i in g.graph['broadcaster'].dest]

        while q:
            root, dest, state = q.pop(0)

            if dest not in g.graph:
                continue

            module = g.graph[dest]

            if module.name == rx and state == 1:
                counts[root] += 1

                if root not in cycle_lengths:
                    cycle_lengths[root] = count
                
                if all(counts.values()):
                    return lcm(cycle_lengths.values())


            if module.type == 'ff':
                if state == 0:
                    module.prev = 1 if module.prev == 0 else 0
                    newstate = 1 if module.prev == 1 else 0
                    for i in module.dest:
                        q.append((module.name, i, newstate))
            else:
                module.prev[root] = state
                newstate = 0 if all(x == 1 for x in module.prev.values()) else 1
                for i in module.dest:
                    q.append((module.name, i, newstate))