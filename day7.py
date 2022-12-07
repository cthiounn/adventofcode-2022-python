from collections import Counter
with open('data/my_input/7.in') as f:
    lines = [  line.strip() for line in f]
import re

num = lambda x :  re.findall(r"\d+",x)


def depth(s):
    return Counter(s)["/"]+1

def generate_all_path(s):
    return { "/".join(s.split("/")[:-1-i]) +"/" for i in range(0,depth(s))}


def part1and2(lines):
    directory="/"
    d=dict()
    for line in lines :
        if " cd " in line :
            _,_,command=line.split(" ")
            if command=="..":
                directory="/".join(directory.split("/")[:-2])+"/"
            elif "/" not in line:
                directory+=command + "/"
            elif command=="/":
                directory="/"
        elif "$" not in  line:
            size=num(line)
            if size:
                _,filename=line.split(" ")
                d[directory+filename]=int(size[0])

    all_d=set()
    for item in list(map(generate_all_path,d.keys())):
        all_d|=item
    returnsum=0
    d_size=dict()
    for dir in all_d:
        dir_size=(sum([i for e,i in d.items() if dir in e]))
        d_size[dir]=dir_size
        if dir_size <= 100000:
            returnsum+=dir_size

    print(sorted(d_size.values()))
    return returnsum

#30000000-(70000000-41412830)
print(part1and2(lines))