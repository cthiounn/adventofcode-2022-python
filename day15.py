import re
from collections import defaultdict

with open("data/my_input/15.in") as f:
    alllines = [line.strip() for line in f if len(line.strip())]

num = lambda x: re.findall(r"-?\d+", x)


def print_grid(d):
    minx = min([x for x, y in d.keys()])
    maxx = max([x for x, y in d.keys()])
    miny = min([y for x, y in d.keys()])
    maxy = max([y for x, y in d.keys()])
    for j in range(miny, maxy + 1):
        st = ""
        for i in range(minx, maxx + 1):
            if (i, j) in d:
                st += d[(i, j)]
            else:
                st += "."
        print(st)


def compute_taxicab_d(x, y, xx, yy):
    return abs(x - xx) + abs(y - yy)


def xy_unfound(x, l):
    for (xx, yy) in l:
        if x in range(xx, yy + 1):
            return False
    return True


def part1and2(alllines, numy):
    dd = defaultdict(list)
    points_to_check = []
    for l in alllines:
        coordinates = num(l)
        if coordinates:
            x, y, xx, yy = list(map(int, coordinates))
            taxicab_d = compute_taxicab_d(x, y, xx, yy)
            for i in range(taxicab_d + 2):
                rayon = taxicab_d - i
                if i == taxicab_d + 1:
                    if 0 <= y + i <= 4000000:
                        points_to_check.append((x, y + i))
                    if 0 <= y - i <= 4000000:
                        points_to_check.append((x, y - i))
                elif i == taxicab_d:
                    if 0 <= y + i <= 4000000:
                        dd[y + i] += [(x, x)]
                        points_to_check.append((x - 1, y + i))
                        points_to_check.append((x + 1, y + i))
                    if 0 <= y - i <= 4000000:
                        dd[y - i] += [(x, x)]
                        points_to_check.append((x - 1, y - i))
                        points_to_check.append((x + 1, y - i))
                else:
                    if 0 <= y + i <= 4000000:
                        dd[y + i] += [(x - rayon, x + rayon)]
                        points_to_check.append((x - rayon - 1, y + i))
                        points_to_check.append((x + rayon + 1, y + i))
                    if 0 <= y - i <= 4000000 and i != 0:
                        dd[y - i] += [(x - rayon, x + rayon)]
                        points_to_check.append((x - rayon - 1, y - i))
                        points_to_check.append((x + rayon + 1, y - i))

    s = set()
    for (x, y) in points_to_check:
        if 0 <= x <= 4000000 and xy_unfound(x, dd[y]):
            print(x, y)
            break
    return len(s), x * 4000000 + y


print(part1and2(alllines, 2000000))
