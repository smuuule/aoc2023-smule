table = {}
def memoize(func):
    def decorator(g, p):
        if p not in table:
            table[p] = func(g, p)
        return table[p]
    
    return decorator

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(self.x + self.y)

class Garden:
    def __init__(self, input, part: int) -> None:
        self.grid = [list(i) for i in input.splitlines()]
        self.height = len(self.grid)
        self.width = len(max(self.grid))
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'S':
                    self.start = Point(x, y)
        self.plots = set([(self.start, (0, 0))])
        self.part = part
    
    def get(self, point):
        if self.part == 2:
            wrapx = divmod(point.x, self.width)
            wrapy = divmod(point.y, self.width)
            return self.grid[wrapy[1]][wrapx[1]], (wrapx[0], wrapy[0])
        elif self.part == 1:
            if 0 <= point.x < self.width and 0 <= point.y < self.height:
                return self.grid[point.y][point.x]
            else:
                return -1
    
    @memoize
    def adjacents(self, point):
        adj = []
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            p = Point(point[0].x + dir[0], point[0].y + dir[1])
            val = self.get(p)
            if self.part == 2:
                if val[0] != '#':
                    adj.append((p, val[1]))
            elif self.part == 1:
                if val[0] not in ['#', -1]:
                    adj.append(p, (0, 0))
        return adj

    def __repr__(self) -> str:
        return f'Size: {self.width}x{self.height}\nStart: {self.start}\nEnd plots: {len(self.plots)}'
    
    def step(self, m):
        prev_plots = self.plots
        new_plots = set()
        for _ in range(m):
            new_plots.clear()
            for p in prev_plots:
                for adj in self.adjacents(p):
                    new_plots.add(adj)

            prev_plots = new_plots.copy()
        
        self.plots = prev_plots

def part1(input):

    g = Garden(input, 1)
    g.step(64)

    return g
    
def part2(input):
    
    g = Garden(input, 2)
    g.step(26501365)

    return g