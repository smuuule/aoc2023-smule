def diffs(lst: list) -> list:
    curr, prev = 0, lst[0]
    result = []
    for i in lst[1:]:
        curr = i
        result.append(curr - prev)
        prev = i
    
    return result

def part1(input):
    count = 0
    for history in input.splitlines():
        lasts = []
        history = list(map(int, history.split()))

        while not all(i == 0 for i in history):
            lasts.append(history[-1])
            history = diffs(history)
        count += sum(lasts)
    
    return count
    
def part2(input):
    count = 0
    for history in input.splitlines():
        first = []
        history = list(map(int, history.split()))

        while not all(i == 0 for i in history):
            first.insert(0, history[0])
            history = diffs(history)
        
        temp = 0
        for i in first:
            temp = i - temp

        count += temp
    
    return count