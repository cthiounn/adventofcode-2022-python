with open('data/my_input/8.in') as f:
    lines = [  line.strip() for line in f]


def left(kk,k):
    a,b=kk
    i,j=k
    return  a<i and b==j



def right(kk,k):
    a,b=kk
    i,j=k
    return  a>i and b==j



def up(kk,k):
    a,b=kk
    i,j=k
    return  a==i and b<j



def down(kk,k):
    a,b=kk
    i,j=k
    return  a==i and b>j

def visible_(v,d):
    return all(v>x for x in d.values())

def findtrees(k,d):
    dleft,dright,dup,ddown= dict(),dict(),dict(),dict()
    for kk,v in d.items():
        if kk==k:
            continue
        elif left(kk,k):
            dleft[kk]=v
        elif right(kk,k):
            dright[kk]=v
        elif down(kk,k):
            ddown[kk]=v
        elif up(kk,k):
            dup[kk]=v
    return dleft,dright,dup,ddown

def visible(k,v,d):
    dleft,dright,dup,ddown=findtrees(k,d)
    return visible_(v,dleft) or visible_(v,dright) or visible_(v,dup) or visible_(v,ddown) 


def scenicpoints(k,v,d):
    stopleft,stopright,stopup,stopdown=False,False,False,False
    vleft,vright,vdown,vup=0,0,0,0
    i,j=k
    increment=0
    while not stopleft or not stopright or not stopup or not stopdown:
        increment+=1
        if not stopright:
            if (i+increment,j) in d and d[(i+increment,j)]<v:
                vright+=1
            else:
                
                if (i+increment,j) in d and d[(i+increment,j)]>=v:
                    vright+=1
                stopright=True 
        
        if not stopleft:
            if (i-increment,j) in d and d[(i-increment,j)]<v:
                vleft+=1
            else:
                if (i-increment,j) in d and d[(i-increment,j)]>=v:
                    vleft+=1
                stopleft=True 

        
        if not stopup:
            if (i,j-increment) in d and d[(i,j-increment)]<v:
                vup+=1
            else:
                if (i,j-increment) in d and d[(i,j-increment)]>=v:
                    vup+=1
                stopup=True 

        
        if not stopdown:
            if (i,j+increment) in d and d[(i,j+increment)]<v:
                vdown+=1
            else:
                if (i,j+increment) in d and d[(i,j+increment)]>=v:
                    vdown+=1
                stopdown=True
    print(k,v,vleft,vright,vdown,vup)        
    return vleft,vright,vdown,vup
def scenic(k,v,d):
    vleft,vright,vdown,vup=scenicpoints(k,v,d)
    return vleft*vright*vdown*vup
def part1and2(lines):
    d=dict()
    for i,line in enumerate(lines):
        for j, char in enumerate(line):
            d[(i,j)]=int(char)
    return len([k for k,v in d.items() if visible(k,v,d)]),max([scenic(k,v,d) for k,v in d.items()])
    
print(part1and2(lines))