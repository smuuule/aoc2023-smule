import numpy as np

def is_symbol(c: str):
    return 

def string_to2D(input: str):
    
    matrix = []
    
    for line in input.splitlines():
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)
    
    return matrix

def adjacent_ints(matrix, coord: tuple):
    x, y = coord
    coords = [(x-1,y-1), (x,y-1), (x+1,y-1),
              (x-1,y), (x,y), (x+1,y),
              (x-1,y+1), (x,y+1), (x+1,y+1)]
    
    
    adjacent = []
    
    for (x, y) in coords:
        if (x < 0) or (x >= len(matrix[0])) or (y < 0) or (y >= len(matrix)):
            continue
        val = matrix[y][x]
        
        if val.isdigit():
            adjacent.append((x, y))
            
    return adjacent

def get_part(matrix, coord):
    l = h = coord[0]
    while (l > 0) and matrix[coord[1]][l-1].isdigit():
        l -= 1
    while (h < len(matrix[0])) and matrix[coord[1]][h].isdigit():
        h += 1
    return ((l, coord[1]), int("".join(matrix[coord[1]][l:h])))
           
def part1(input):
    
    matrix = string_to2D(input)
    symbols = []
    
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if not(char.isdigit() or (char == '.')):
                symbols.append((x,y))
                
    partSet = set()
    for symbol in symbols:
        for adjacent in adjacent_ints(matrix, symbol):
            partSet.add(get_part(matrix, adjacent))
    
    return sum([int(i[1]) for i in partSet])
    
def part2(input):
    
    matrix = string_to2D(input)
    symbols = []
    
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == '*':
                symbols.append((x,y))
                
    gearRatios = 0
    for symbol in symbols:
        symbolSet = set()
        for adjacent in adjacent_ints(matrix, symbol):
            
            symbolSet.add(get_part(matrix, adjacent))
            
        if len(symbolSet) == 2:
            gearRatios += (list(symbolSet)[0][1] * list(symbolSet)[1][1])
    
    return gearRatios