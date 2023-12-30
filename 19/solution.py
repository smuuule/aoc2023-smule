from copy import deepcopy


class Rating:
    def __init__(self, attr_str):
        attr = [int(x[2:]) for x in attr_str[1:-1].split(',')]
        self.x = attr[0]
        self.m = attr[1]
        self.a = attr[2]
        self.s = attr[3]
    
    def __repr__(self) -> str:
        return "x: %s, m: %s, a: %s, s: %s," % (self.x, self.m, self.a, self.s)

    def get(self, key: str):
        match key:
            case 'x': return self.x
            case 'm': return self.m
            case 'a': return self.a
            case 's': return self.s
    
    def sum(self):
        return self.x + self.m + self.a + self.s

    def follows(self, rule):
        if '>' in rule:
            rule = rule.split(':')[0].split('>')
            return self.get(rule[0]) > int(rule[1])
        elif '<' in rule:
            rule = rule.split(':')[0].split('<')
            return self.get(rule[0]) < int(rule[1])
        else:
            return True

    def apply(self, rule, rules):
        if rule == 'A' or rule == 'R':
            return rule
        else:
            for r in rules[rule]:
                if self.follows(r):
                    if ':' in r:
                        return self.apply(r.split(':')[1], rules)
                    else:
                        return self.apply(r, rules)        

def part1(input):
    rules_l, ratings_l = [x.splitlines() for x in input.split('\n\n')]
    rules = {}

    for rule in rules_l:
        name, rest = rule.split('{')
        rest = rest[:-1].split(',')
        rules[name] = rest
    
    tot = 0
    for i in ratings_l:
        rating = Rating(i)
        if rating.apply('in', rules) == 'A':
            tot += rating.sum()

    return tot



    
def part2(input):

    rules_l, _ = [x.splitlines() for x in input.split('\n\n')]
    rules = {}

    for rule in rules_l:
        name, rest = rule.split('{')
        rest = rest[:-1].split(',')
        rules[name] = rest

    def xmas_sum(xmas):
        sum = 1
        for l, h in xmas.values():
            sum *= (h-l + 1)
        return sum

    def apply_range(xmas, rule):
        print(xmas, rule)
        tot = 0
        if ':' not in rule:
            if rule == 'A':
                tot += xmas_sum(xmas)
                return tot
            elif rule == 'R':
                return tot
        for rule in rules[rule]:
            if ':' in rule:
                new = deepcopy(xmas)
                if '>' in rule:
                    rule, dest = rule.split(':')
                    rule = rule.split('>')
                    if new[rule[0]][1] > int(rule[1]):
                        new[rule[0]][0] = max(xmas[rule[0]][0], int(rule[1]) + 1)
                        tot += apply_range(new, dest)

                elif '<' in rule:
                    rule, dest = rule.split(':')
                    rule = rule.split('<')
                    if new[rule[0]][0] < int(rule[1]):
                        print("test")
                        new[rule[0]][1] = min(xmas[rule[0]][1], int(rule[1]) - 1)
                        tot += apply_range(new, dest)
            else:
                if rule == 'A':
                    tot += xmas_sum(xmas)
                elif rule == 'R':
                    continue
                else:
                    tot += apply_range(xmas, rule)
                    
        return tot

    
    return apply_range({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in')