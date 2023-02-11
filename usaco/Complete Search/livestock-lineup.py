from collections import defaultdict
from os import remove


def input_parser(file):
    return [line.rstrip() for line in open(file)]


def milk_order():
    lines = input_parser('lineup.out')
    constraints = defaultdict(set)
    c = {"Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"}
    for line in lines[1:]:
        a, b = line.split(' must be milked beside ')
        constraints[a].add(b)
        constraints[b].add(a)

    def try_all(cows, part):
        if len(cows) == 0:
            res.add(tuple(part))
        for cc in constraints[part[0]].difference({part[1]}):
            try_all(cows.difference({cc}), [cc] + part)

        for cc in constraints[part[-1]].difference({part[-2]}):
            try_all(cows.difference({cc}), part + [cc])

    res = set()
    for cow, adj in constraints.items():
        if len(adj) == 2:
            c.remove(cow)
            for v in constraints[cow]:
                try_all(c.difference({v}), [v, cow])
                try_all(c.difference({v}), [cow, v])
            break

    return sorted(res)[0]


txt = """3
Buttercup must be milked beside Bella
Blue must be milked beside Bella
Sue must be milked beside Beatrice
"""
with open("lineup.out", "w") as f:
    f.write(txt)

print(milk_order())

remove("lineup.out")
