inf = float("inf")

def dijkstra(grid, start):
    height, width = len(grid), len(grid[0])
    x, y = start
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    cost_map = [[inf]*width for _ in range(height)]
    cost_map[y][x] = 0
    closed = set()
    q = [(start, 0)]
    
    while q:
        (x, y), cost = q.pop()
        if (x, y, cost) in closed:
            continue
        closed.add((x, y, cost))
        for i, j in adj:
            #TODO
            continue
        
    return cost

def part1(input):
    grid = [[int(j) for j in list(i)] for i in input.splitlines()]
    
    return dijkstra(grid, (0, 0))
    
def part2(input):
    
    return "TODO part 2"