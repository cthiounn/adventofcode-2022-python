from collections import Counter
with open('data/my_input/6.in') as f:
    lines = [  line.strip() for line in f]




def part1and2(lines,num):
    for i in range(len(lines)):
        if len(Counter(lines[i:i+num]))==num:
            return i+num
    return 0

print(part1and2(lines[0],4))
print(part1and2(lines[0],14))