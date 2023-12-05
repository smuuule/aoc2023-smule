def find_lowest_location(options, mapRanges):
    mapRanges.reverse()
    end = 0
    foundLowest = False
    while(not foundLowest):
        curr = end
        for map in mapRanges:
            for mapRange in map:
                if mapRange[0] <= curr < (mapRange[0] + mapRange[2]):
                    curr = mapRange[1] + (curr - mapRange[0])
                    break
            
        for seedRange in options:
            if seedRange[0] <= curr < seedRange[0]+seedRange[1]:
                foundLowest = True
                
        end += 1
    
    return end-1

def parse(input):
    options = []
    options, *maps = input.split("\n\n")
    options = [int(i) for i in options[6:].split()]
    
    mapRanges = []
    for mapRange in maps:
        mapRanges.append([list(map(int,i)) for i in [i.split() for i in mapRange.split("\n")][1:]])
        
    return options, mapRanges

def get_pairs(lst):
    if (len(lst) < 2) or (len(lst) % 2 != 0):
        raise Exception("List has to be bigger than 1 and even length")
    new = []
    i = 0
    j = 1
    while j < len(lst):
        new.append((lst[i], lst[j]))
        i += 2
        j += 2
        
    return new

def part1(input):
    
    options, mapRanges = parse(input)

    options = [(i, 1) for i in options]
        
    return find_lowest_location(options, mapRanges)
    
def part2(input):
    options, mapRanges = parse(input)
    options = [(val, options[i+1]) for i, val in list(enumerate(options))[::2]]
        
    return find_lowest_location(options, mapRanges)