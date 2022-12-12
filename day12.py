from collections import deque
with open('data/my_input/12.in') as f:
    lines = [  line.strip() for line in f]


def part1and2(lines):
    dmap=dict()
    startingpositions=deque()
    for i,l in enumerate(lines) :
        for j,c in enumerate(l):
            if c=="S":
                x,y=i,j
                dmap[(i,j)]='a'
                startingpositions.appendleft((i,j))
            else:
                if c=='a':
                    startingpositions.append((i,j))
                dmap[(i,j)]=c
    allpath=[]
    for s in startingpositions:
        x,y=s
        startingposition=(0,x,y)
        position_to_evaluate=deque()
        position_to_evaluate.append(startingposition)
        already_visited={(x,y):0}
        
        while position_to_evaluate:
            pos=position_to_evaluate.popleft()
            cost,x,y=pos
            newcost=cost+1
            char=dmap[(x,y)]
            charpos=ord(char)
            for di in {-1,1}:
                if ((x+di,y) in dmap and dmap[(x+di,y)]=="E" and char=='z' ) :
                    allpath.append(newcost)
                    position_to_evaluate=[]
                elif (x+di,y) in dmap and charpos+1>=ord(dmap[(x+di,y)]):
                    if (x+di,y) in already_visited:
                        if already_visited[(x+di,y)]>newcost:
                            position_to_evaluate.append((newcost,x+di,y))
                            already_visited[(x+di,y)]=newcost
                    else:
                        already_visited[(x+di,y)]=newcost
                        position_to_evaluate.append((newcost,x+di,y))



                if ((x,y+di) in dmap and dmap[(x,y+di)]=="E" and char=='z'):
                    allpath.append(newcost)
                    position_to_evaluate=[]
                elif (x,y+di) in dmap and charpos+1>=ord(dmap[(x,y+di)]):
                    if (x,y+di) in already_visited:
                        if already_visited[(x,y+di)]>newcost:
                            position_to_evaluate.append((newcost,x,y+di))
                            already_visited[(x,y+di)]=newcost
                    else:
                        already_visited[(x,y+di)]=newcost
                        position_to_evaluate.append((newcost,x,y+di))
    return allpath[0],min(allpath)
print(part1and2(lines))