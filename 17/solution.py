from heapq import heappop, heappush

inf = float("inf")

def dijkstra(grid, start, min_straight=1, max_straight=3):
    height, width = len(grid), len(grid[0])
    x, y = start
    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    cost_map = [[inf]*width for _ in range(height)]
    cost_map[y][x] = 0
    closed = set()
    q = [(0, start, (0, 0))]
    
    while q:
        cost, (x, y), (iprev, jprev) = heappop(q)
        if (x, y, iprev, jprev) in closed:
            continue
        closed.add((x, y, iprev, jprev))
        for i, j in adj:
            costnext = cost
            if (i == iprev and j == jprev) or (i == -iprev and j == -jprev):
                continue
             
            if (0 <= (x + i * (min_straight-1)) < width) and (0 <= (y + j * (min_straight-1)) < height):
                for s in range(1, min_straight):
                    xnext, ynext = x + i*s, y + j*s
                    costnext += grid[ynext][xnext]
        
            for straight in range(min_straight, max_straight+1):
                xnext, ynext = x + (i * straight), y + (j * straight)
                if 0 <= xnext < width and 0 <= ynext < height:
                    costnext += grid[ynext][xnext]
                    if costnext < cost_map[ynext][xnext]:
                        cost_map[ynext][xnext] = costnext
                    heappush(q, (costnext, (xnext, ynext), (i, j)))
                else:
                    break

    return cost_map[-1][-1]

def part1(input):
    grid = [[int(j) for j in list(i)] for i in input.splitlines()]
    
    return dijkstra(grid, (0, 0))
    
def part2(input):
    grid = [[int(j) for j in list(i)] for i in input.splitlines()]
    
    return dijkstra(grid, (0, 0), 4, 10)