seen = set()

def base_case(grid, pos, dir):
    next = (pos[0]+dir[0], pos[1]+dir[1])
    if not (0 <= next[0] < len(grid[0]) and 0 <= next[1] < len(grid)):
        seen.add((pos, dir))
        return True
    if (pos, dir) in seen:
        return True
    
    return False

def beam(grid, pos, dir):
    next = (pos[0]+dir[0], pos[1]+dir[1])
    if base_case(grid, pos, dir): return
    
    val = grid[next[1]][next[0]]
    if not (pos[0] in [-1, len(grid)] or pos[1] in [-1, len(grid[0])]):
        seen.add((pos, dir))
    if val == '.':
        while val == '.': # workaround because of python's recursion limit
            pos = next
            next = (pos[0]+dir[0], pos[1]+dir[1])
            if base_case(grid, pos, dir): return
            val = grid[next[1]][next[0]]
            seen.add((pos, dir))
    if val == '/':
        #(1, 0) <=> (0, -1)
        #(-1, 0) <=> (0, 1)
        return beam(grid, next, (-1 * dir[1], -1 * dir[0]))
    if val == '\\':
        #(1, 0) <=> (0, 1)
        #(-1, 0) <=> (0, -1)
        return beam(grid, next, (dir[1], dir[0]))
    if val == '-':
        #(1, 0) => (1, 0)
        #(-1, 0) => (-1, 0)
        #(0, 1), (0, -1) => (1, 0) & (-1, 0)
        if dir[0] != 0:
            return beam(grid, next, dir)
        else:
            return beam(grid, next, (-1, 0)), beam(grid, next, (1, 0))
    if val == '|':
        #(0, 1) => (0, 1)
        #(0, -1) => (0, -1)
        #(1, 0), (-1, 0) => (0, 1) & (0, -1)
        if dir[0] == 0:
            return beam(grid, next, dir)
        else:
            return beam(grid, next, (0, -1)), beam(grid, next, (0, 1))

def part1(input):
    grid = [list(i) for i in input.splitlines()]
    beam(grid, (-1, 0), (1, 0))
    energized = set()
    for (pos, _) in seen:
        energized.add(pos)
    return f'Done, energized {len(energized)} tiles, {100 * len(energized)//(len(grid)*len(grid[0]))}% covered'
    
def part2(input):
    grid = [list(i) for i in input.splitlines()]
    width = len(grid[0])
    height = len(grid)
    record = (0, 0, 0)
    for i in range(-1, height+1):
        for j in range(-1, width+1):
            if i in [-1, height] or j in [-1, width]:
                if i == -1:
                    dir = (0, 1)
                elif i == height:
                    dir = (0, -1)
                elif j == -1:
                    dir = (1, 0)
                elif j == width:
                    dir = (-1, 0)
                beam(grid, (j, i), dir)
                energized = set()
                for (pos, _) in seen:
                    if -1 not in pos:
                        energized.add(pos)
                if len(energized) > record[2]:
                    record = (i, j, len(energized), energized)
                seen.clear()
                
    return f'Done, energized {record[2]} tiles using row {record[0]} and column {record[1]}, {100 * record[2]//(len(grid)*len(grid[0]))}% covered'
