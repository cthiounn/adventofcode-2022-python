import re
from collections import defaultdict
with open("data/my_input/15.in") as f:
    alllines = [line.strip() for line in f if len(line.strip())]

num= lambda x : re.findall(r"-?\d+",x)



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

def compute_taxicab_d(x,y,xx,yy):
    return abs(x-xx)+abs(y-yy)

def decompose(a,b):
    if a ==b :
        return None, a, None
    x,y=a
    xx,yy=b
    if x==xx:
        left=None
        nextx=xx
    elif x<xx:
        left=(x,xx-1)
        nextx=xx
    else:
        left=(xx,x-1)
        nextx=x

    if y==yy:
        right=None
        prevy=y
    elif y<yy:
        right=(y+1,yy)
        prevy=y
    else:
        right=(yy+1,y)
        prevy=yy
    if nextx>prevy:
        return a,None,b
    return left,(nextx,prevy),right

def part1and2(alllines,numy):
    d=dict()
    dd=defaultdict(list)
    for l in alllines:
        coordinates=num(l)
        if coordinates:
            x,y,xx,yy=list(map(int,coordinates))
            taxicab_d=compute_taxicab_d(x,y,xx,yy)
            for i in range(taxicab_d):
                rayon=taxicab_d-i
                if i!=0:
                    if y+i==numy :
                        dd[y+i]+=[(x-rayon,x+rayon)]
                        break
                    if y-i==numy :
                        dd[y-i]+=[(x-rayon,x+rayon)]
                        break
                else:
                    if y==numy :
                        dd[y]+=[(x-rayon,x+rayon)]
                        break
            d[(x,y)]="S"
            d[(xx,yy)]="B"
    lr=dd[numy]
    s=set()
    for i in range(len(lr)):
        a,b =lr[i]
        s|=set(range(a,b))
    # for _ in range(1000):
    #     stop=False
    #     for i in range(len(lr)):
    #         if not stop:
    #             for j in range(i+1,len(lr)):
    #                 a,b,c = decompose(lr[i],lr[j])
    #                 if b is not None :
    #                     stop=True
    #                     lr[i]=a
    #                     lr[j]=c
    #                     lr.append(b)
    #                     while None in lr:
    #                         lr.remove(None)
    #                     break
        
    
    # print(lr)
    
    return len(s)
print(part1and2(alllines,2000000))
