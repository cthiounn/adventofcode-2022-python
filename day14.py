import re
from collections import deque
with open("data/my_input/14.in") as f:
    alllines = [line.strip() for line in f if len(line.strip())]

num= lambda x : re.findall(r"\d+",x)

def buildmap(d,l):
    all_int=deque(map(int,num(l)))

    x=all_int.popleft()
    y=all_int.popleft()
    while all_int:
        
        xx=all_int.popleft()
        yy=all_int.popleft()
        if xx==x:
            if y<yy:
                r=range(y,yy+1)
            else:
                r=range(yy,y+1)
            for i in r:
                d[(x,i)]='#'
        elif yy==y:
            if x<xx:
                r=range(x,xx+1)
            else:
                r=range(xx,x+1)
            for i in r:
                d[(i,y)]='#'
        x=xx
        y=yy
    

def print_grid(d):
    minx=min([x for x,y in d.keys()])
    maxx=max([x for x,y in d.keys()])
    miny=min([y for x,y in d.keys()])
    maxy=max([y for x,y in d.keys()])
    for j in range(miny,maxy+1):
        st=""
        for i in range(minx,maxx+1):
            if (i,j) in d :
                st+=d[(i,j)]
            else:
                st+="."
        print(st)

def part1and2(alllines):
    dd=dict()
    for l in alllines:
        buildmap(dd,l)

    source=(500,0)
    sourcex,sourcey=source

    d=dd.copy()
    abyss_level= max([ y for x,y in d.keys()])
    abyss_level_reached=False
    while not abyss_level_reached:
        newx,newy=sourcex,sourcey
        newpoint=False
        while not (abyss_level_reached or newpoint):
            
            if (newx,newy+1) in d and (newx-1,newy+1) in d and (newx+1,newy+1) in d:
                d[(newx,newy)]='o'
                newpoint=True
            elif (newx,newy+1) in d and (newx-1,newy+1) in d:
                newx+=1
            elif (newx,newy+1) in d and (newx+1,newy+1) in d:
                newx-=1
            elif (newx,newy+1) in d:
                newx-=1
            abyss_level_reached=(newy>=abyss_level)
            newy+=1

    part1=sum([1 for v in d.values() if v=='o'])

    
    d=dd.copy()
    abyss_level= max([ y for x,y in d.keys()])+2
    
    for i in range(-1000,1000):
        d[(i,abyss_level)]="#"
    
    while (sourcex,sourcey) not in d :
        newx,newy=sourcex,sourcey
        newpoint=False
        while not newpoint:
            
            if (newx,newy+1) in d and (newx-1,newy+1) in d and (newx+1,newy+1) in d:
                d[(newx,newy)]='o'
                newpoint=True
            elif (newx,newy+1) in d and (newx-1,newy+1) in d:
                newx+=1
            elif (newx,newy+1) in d and (newx+1,newy+1) in d:
                newx-=1
            elif (newx,newy+1) in d:
                newx-=1
            newy+=1

    return  part1,sum([1 for v in d.values() if v=='o'])

print(part1and2(alllines))
