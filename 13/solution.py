def symmetric_hori(matrix, middle):
    l = middle
    h = middle + 1
    if l < 0 or h >= len(matrix):
        return False

    while matrix[l] == matrix[h]:
        l -= 1
        h += 1
        if l < 0 or h >= len(matrix):
            return True
        
    return False

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]

def part1(input):
    sum = 0
    for grid in input.split('\n\n'):
        matrix = []
        for line in grid.splitlines():
            matrix.append(line)

        for between in range(len(transpose(matrix))):
            if symmetric_hori(transpose(matrix), between):
                sum += (between+1)

        for between in range(len(matrix)):
            if symmetric_hori(matrix, between):
                sum += (between+1)*100

    return sum
    
def part2(input):
    
    count = 0
    for grid in input.split('\n\n'):
        matrix = []
        old_h = -1
        old_v = -1
        for line in grid.splitlines():
            matrix.append(line)

        for between in range(len(transpose(matrix))):
            if symmetric_hori(transpose(matrix), between):
                old_v = between

        for between in range(len(matrix)):
            if symmetric_hori(matrix, between):
                old_h = between

        for y in range(len(matrix)):
            for x, curr in enumerate(matrix[y]):
                if curr == '.':
                    matrix[y] = matrix[y][:x] + '#' + matrix[y][x+1:]
                else:
                    matrix[y] = matrix[y][:x] + '.' + matrix[y][x+1:]

                tmp = 0
                for between in range(len(transpose(matrix))):
                    if between != old_v:
                        if symmetric_hori(transpose(matrix), between):
                            tmp += (between+1)

                for between in range(len(matrix)):
                    if between != old_h:
                        if symmetric_hori(matrix, between):
                            tmp += (between+1)*100
                
                matrix[y] = matrix[y][:x] + curr + matrix[y][x+1:]
                if tmp != 0:
                    break
            
            else:
                continue
            break

        count += tmp
        
    return count