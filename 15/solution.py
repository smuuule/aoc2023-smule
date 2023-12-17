hashmap = [[] for _ in range(256)]

def hash(string) -> int:
    curr = 0
    for c in string:
        ascii = ord(c)
        curr = 17 * (curr + ascii) % 256
    return curr

def remove(key):
    box = hashmap[hash(key)]
    if key in (keys := [key for key, _ in box]):
        box.pop(keys.index(key))

def insert(key, val):
    box = hashmap[hash(key)]
    if key in (keys := [key for key, _ in box]):
        box[keys.index(key)] = (key, val)
    else:
        box.append((key, val))

def part1(input):

    return sum([hash(i) for i in input.split(',')])
    
def part2(input):
    for step in input.split(','):
        if '=' in step:
            step = step.split('=')
            insert(step[0],step[1])
        else:
            remove(step[:-1])

    power = 0
    for i, box in enumerate(hashmap):
        for j, lens in enumerate(box):
            power += (i+1) * (j+1) * int(lens[1])

    return power