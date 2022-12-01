with open('data/my_input/1.in') as f:
    lines = f.read().split("\n\n")

def part1(vlines):
    return max([sum(
        list(map(int, i.split("\n")))) for i in vlines])

def part2(vlines):
    return sum(sorted([sum(
        list(map(int, i.split("\n")))) for i in vlines],reverse=True)[:3])

print(part1(lines))
print(part2(lines))