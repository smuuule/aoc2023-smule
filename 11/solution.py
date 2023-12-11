from tqdm import tqdm

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]

def expand(matrix):

    rows = []
    for i,line in enumerate(matrix):
        if line.count('.') == len(line):
            if i < len(line):
                rows.append(i)
            else:
                rows.append(i+1)

    new_matrix = matrix
    for i, index in enumerate(rows):
        new_matrix.insert(index+i, ['.' for i in range(len(line))])

    matrix_t = transpose(matrix)
    cols = []
    for i,line in enumerate(matrix_t):
        if line.count('.') == len(line):
            if i < len(line):
                cols.append(i)
            else:
                cols.append(i+1)
    
    new_matrix = transpose(new_matrix)
    for i, index in enumerate(cols):
        new_matrix.insert(index+i, ['.' for i in range(len(line))])

    return transpose(new_matrix)

def part1(input):
    matrix = []
    for line in input.splitlines():
        matrix.append([*line])

    matrix = expand(matrix)
    coords = []
    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c == '#':
                matrix[i][j] = str(len(coords)+1)
                coords.append((j, i))


    pairs = [(a, b) for i, a in enumerate(coords) for b in coords[i + 1:]]
    count = 0
    for pair in pairs:
        a, b = pair
        count += abs(a[0] - b[0]) + abs(a[1] - b[1])

    return count
    
def part2(input):
    
    return "TODO part 2"