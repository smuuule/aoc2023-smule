def getWins(card: list) -> int:
    winning, gotten = [i.split( ) for i in card.split(': ')[1].split(' | ')]
            
    return sum(1 for i in winning if i in gotten)

def part1(input):
    winnings = [2**(getWins(card)-1) for card in input.splitlines() if getWins(card) > 0]
    
    return sum(winnings)
    
def part2(input):
    lines = input.splitlines()
    copies = [1] * len(lines)
    
    for i, card in enumerate(lines):
        for copy in range(i, i+getWins(card)):
            copies[copy+1] += copies[i]
    
    return sum(copies)