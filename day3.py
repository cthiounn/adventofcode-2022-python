from collections import Counter

with open('data/my_input/3.in') as f:
    lines = [  line.strip() for line in f]


def split_compute(line):
    a,b= line[:len(line)//2],line[len(line)//2:]
    a_count=Counter(a)
    b_count=Counter(b)
    inter= a_count&b_count
    sum=0
    for i,j in inter.items():
        if i.islower():
            sum+=ord(i)-96
        else:
            sum+=ord(i)-64+26
    return sum

def split_compute2(l1,l2,l3):
    a_count=Counter(l1)
    b_count=Counter(l2)
    c_count=Counter(l3)
    inter= a_count&b_count&c_count
    sum=0
    for i,j in inter.items():
        if i.islower():
            sum+=ord(i)-96
        else:
            sum+=ord(i)-64+26
    return sum

def part1(vlines):
    return sum(list(map(split_compute,vlines)))

def part2(vlines):
    return sum([split_compute2(*vlines[3*i-3:3*i]) for i in range(1,len(vlines)//3+1)])



print(part1(lines))
print(part2(lines))