from functools import cmp_to_key

types = {'11111':'high', '1112':'pair', '122':'2pair', '113':'three', '23':'house', '14':'four', '5':'five'}
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def eval_hand(hand):
    handDict = dict()
    for i in hand:
        handDict[i] = handDict.get(i, 0) + 1
        
    
    handString = ''.join(map(str, sorted(list(handDict.values()))))
        
    return handString, handDict

def sort_hands(hand: str):
    return list(types.values()).index(hand[0])

def compare_hands(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    i = 0
    while i < len(hand1):
        card1 = hand1[i]
        card2 = hand2[i]
        if card1 != card2:
            return 1 if cards.index(card1) < cards.index(card2) else -1
        
        i += 1
    
    return -1

def joker_parse(hand):
    string, handDict = eval_hand(hand)
    hand = dict(sorted(handDict.items(), key=lambda i: i[1]))
    jokerHand = hand
    jokerAmount = jokerHand.pop('J', 0)
    if jokerAmount == 0:
        return string
    elif jokerAmount == 5:
        return '5'

    jokerHand[max(hand, key=hand.get)] += jokerAmount
        
    return ''.join(map(str, sorted(list(jokerHand.values()))))

def hands_to_total(hands: list) -> int:
    hands.sort(key=sort_hands)
    
    groups = [[], [], [], [], [], [], []]
    for hand in hands:
        for i in range(0, len(groups)):
            if hand[0] == list(types.values())[i]:
                groups[i].append([hand[1], hand[2]])
                break
        
            
    total = 0
    rank = 1
    for group in groups:
        group.sort(key=cmp_to_key(compare_hands))
        for hand in group:
            total += rank * int(hand[1])
            rank += 1
    
    return total

def part1(input):
    hands = []
    for i in input.splitlines():
        hand, bid = i.split()
        hands.append((types[eval_hand(hand)[0]], hand, bid))
    
    return hands_to_total(hands)
    
def part2(input):
    global cards
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    hands = []
    for i in input.splitlines():
        hand, bid = i.split()
        hands.append((types[joker_parse(hand)], hand, bid))
    
    return hands_to_total(hands)