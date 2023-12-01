def part1(input):
    
    output = 0
    for line in input.splitlines():
        i = 0
        j = len(line) - 1
        while not line[i].isdigit():
            i += 1
        while not line[j].isdigit():
            j -= 1
        output += int(line[i] + line[j])
    
    return output

def part2(input):
    
    def checkNumber(line, index) -> bool:
        numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
        for i, word in enumerate(numbers):
            if line[index:index+len(word)] == word:
                return (True, str(i+1))
        
        return (False, str(i+1))
    
    output = 0
    for line in input.splitlines():
        i = 0
        j = len(line) - 1
        while not line[i].isdigit() and not checkNumber(line, i)[0]:
            i += 1
        while not line[j].isdigit() and not checkNumber(line, j)[0]:
            j -= 1
            
        first = line[i]
        last = line[j]
            
        if not first.isdigit():
            first = checkNumber(line, i)[1]
            
        if not last.isdigit():
            last = checkNumber(line, j)[1]
            
        output += int(first + last)
    
    
    return output