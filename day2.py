with open('data/my_input/2.in') as f:
    lines = [  line.strip() for line in f]


def parse_and_compute(line):
    i,j=line.split(" ")
    sum=0
    if "Y" in j:
        sum=2
        if "A" in i:
            sum+=6
        elif "B" in i:
            sum+=3
        elif "C" in i:
            sum+=0
    elif "Z" in j:
        sum=3
        if "A" in i:
            sum+=0
        elif "B" in i:
            sum+=6
        elif "C" in i:
            sum+=3
    elif "X" in j:
        sum=1
        if "A" in i:
            sum+=3
        elif "B" in i:
            sum+=0
        elif "C" in i:
            sum+=6

    return sum

def parse_lose_and_compute(line):
    i,j=line.split(" ")
    sum=0
    if "Y" in j:
        sum+=3
        if "A" in i:
            sum+=1
        elif "B" in i:
            sum+=2
        elif "C" in i:
            sum+=3
    elif "Z" in j:
        sum+=6
        if "A" in i:
            sum+=2
        elif "B" in i:
            sum+=3
        elif "C" in i:
            sum+=1
    elif "X" in j:
        if "A" in i:
            sum+=3
        elif "B" in i:
            sum+=1
        elif "C" in i:
            sum+=2

    return sum

def part1(vlines):
    return sum(map(parse_and_compute,vlines))

def part2(vlines):
    return sum(map(parse_lose_and_compute,vlines))

print(part1(lines))
print(part2(lines))