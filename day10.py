with open('data/my_input/10.in') as f:
    lines = [  line.strip() for line in f]

import re

num=lambda x: re.findall(r'-?\d+',x)

def check_lit(i,x,ll):
    if i == x or i ==x+1 or i==x+2:
        ll.append("#")
    else:
        ll.append(".")
def part1and2(lines):
    l=[1]
    x=1
    l.append(x)
    i=1
    ll=[]

    for line in lines:

        check_lit(i,x,ll)
        if "noop" in line:
            l.append(x)
            i+=1
            i%=40
        else:
            
            l.append(x)
            i+=1
            i%=40

            check_lit(i,x,ll)
            x+=int(num(line)[0])
            l.append(x)
            i+=1
            i%=40
        

    print("".join(ll[:40]))
    print("".join(ll[40:80]))
    print("".join(ll[80:120]))
    print("".join(ll[120:160]))
    print("".join(ll[160:200]))
    print("".join(ll[200:240]))
    return l[20]*20+l[60]*60+l[100]*100+l[140]*140+l[180]*180+l[220]*220
    
print(part1and2(lines))