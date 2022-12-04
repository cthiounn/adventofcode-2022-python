import re
with open('data/my_input/4.in') as f:
    lines = [  line.strip() for line in f]

num=lambda x : re.findall(r'\d+',x)


def part1and2(lines):
    sum=0
    sum2=0
    for line in lines:
        a,b,c,d= list(map(int,num(line)))
        r=range(a,b+1)
        r2=range(c,d+1)
        if set(r)&set(r2):
            sum2+=1
        if c>=a and c<=b and a<=d and d <=b:
            sum+=1
        elif a>=c and a<=d and c<=b and b <=d:
            sum+=1
    return sum,sum2

print(part1and2(lines))