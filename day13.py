from functools import cmp_to_key

with open("data/my_input/13.in") as f:
    lines = [line.split("\n") for line in f.read().split("\n\n")]

with open("data/my_input/13.in") as f:
    alllines = [line.strip() for line in f if len(line.strip())]


def lessthan(a, b):
    if type(a) == str:
        a = eval(a)
    if type(b) == str:
        b = eval(b)
    match (a, b):
        case (list(), list()):
            for x, y in zip(a, b):
                if lessthan(x, y) == 0:
                    continue
                return lessthan(x, y)
            return len(a) - len(b)
        case (int(), list()):
            return lessthan([a], b)
        case (list(), int()):
            return lessthan(a, [b])
        case (int(), int()):
            return a - b


def part1and2(lines, alllines):
    somme = 0
    for i, l in enumerate(lines):
        a, b = l
        if lessthan(a, b) < 0:
            somme += i + 1

    newlinea = "[[2]]"
    newlineb = "[[6]]"
    alllines.append(newlinea)
    alllines.append(newlineb)
    alllines.sort(key=cmp_to_key(lessthan))
    return somme, (alllines.index(newlinea) + 1) * (alllines.index(newlineb) + 1)


print(part1and2(lines, alllines))
