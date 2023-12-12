table = {}
def memoize(func):
    def decorator(a, b):
        if (a, b) not in table:
            table[(a, b)] = func(a, b)
        return table[(a, b)]
    
    return decorator

@memoize
def options(springs, contin):
    # Base case
    if len(contin) == 0:
        return "#" not in springs
    if springs == "":
        return len(contin) == 0
    elif contin[0] > len(springs):
        return 0
    
    # Continure to next if empty
    if springs[0] == '.':
        return options(springs[1:], contin)

    elif springs[0] == '#':
        # If the contin size wouldn't fit, we skip our other checks and return 0
        if all(springs[i] != '.' for i in range(contin[0])):
            # If we are at the end and we can use our last remaining springs,
            # there's only 1 option
            if len(springs) == contin[0]:
                if len(contin) == 1:
                    return 1
                else:
                    return 0
            if springs[contin[0]] != "#":
                return options("." + springs[contin[0] + 1:], contin[1:])
            
        return 0
        
    # If we don't know ('?'), count all options using both '.' and '#'
    else:
        return options('.' + springs[1:], contin) + options('#' + springs[1:], contin)

def part1(input):
    count = 0
    for row in input.splitlines():
        springs, contin = row.split()
        contin = list(map(int, contin.split(',')))
        count += options(springs, contin)
    
    return count
    
def part2(input):
    count = 0
    for row in input.splitlines():
        springs, contin = row.split()
        # --- Part 2 specific
        springs = ((springs + '?') * 5)[:-1]
        contin = ((contin + ',') * 5)[:-1]
        # ---
        contin = list(map(int, contin.split(',')))

        count += options(springs, tuple(contin))
    
    return count