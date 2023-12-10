def input_to_matrix(input):
    matrix = []
    start = ()
    for i, line in enumerate(input.splitlines()):
        if 'S' in line:
            start = (line.index('S'), i)
        matrix.append([*line])
        
    return matrix, start

def directions(pipe):
    match pipe:
        case '|': return [(0, -1), (0, 1) ]
        case '-': return [(1, 0) , (-1, 0)]
        case 'L': return [(0, -1), (1, 0) ]
        case 'J': return [(0, -1), (-1, 0)]
        case '7': return [(0, 1) , (-1, 0)]
        case 'F': return [(0, 1) , (1, 0) ]
        case '.': return []
        
def inverse_direction(dir: tuple) -> tuple:
    i,j = dir
    return (-i, -j)
        
def get_start_pipe(matrix, start):
    x, y = start
        
    for pipe in ['|', '-', 'F', 'J', 'L', '7']:
        possible = []
        for dir in directions(pipe):
            if not (0 <= y+dir[1] < len(matrix) and 0 <= x+dir[0] < len(matrix[0])):
                continue
            if inverse_direction(dir) in directions(matrix[y+dir[1]][x+dir[0]]):
                possible.append(1)
                
        if sum(possible) == 2:
            return pipe
        
    return -1

def part1(input, part2=False):
    matrix, start = input_to_matrix(input)
    start_pipe = get_start_pipe(matrix, start)
    iprev = start
    jprev = start
    i, j = [tuple(map(sum, zip(x, start))) for x in directions(start_pipe)]
    count = 1
    seen = [start, i, j]
    while i != j:
        inext = [tuple(map(sum, zip(x, i))) for x in directions(matrix[i[1]][i[0]])]
        inext.remove(iprev)
        iprev = i
        i = inext[0]
        if i not in seen:
            seen.append(i)
        
        jnext = [tuple(map(sum, zip(x, j))) for x in directions(matrix[j[1]][j[0]])]
        jnext.remove(jprev)
        jprev = j
        j = jnext[0]
        if j not in seen:
            seen.append(j)
                
        count += 1
    
    if part2: return matrix, seen
    
    return count
    
def part2(input):
    matrix, seen = part1(input, True)
    count = 0
    for i in range(len(matrix)):
        inner = False
        for j in range(len(matrix[0])):
            if (j, i) in seen:
                if matrix[i][j] in 'LJ|':
                    inner = not inner
                continue
            if inner:
                count += 1
    
    return count