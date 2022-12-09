with open('data/my_input/9.in') as f:
    lines = [  line.strip() for line in f]

def move_tail(current_pos_tail,current_pos_head):
    xx,yy=current_pos_head
    x,y=current_pos_tail
    valid=False
    for i in range(-1,2):
        for j in range(-1,2):
            if not valid:
                if (x+i,y+j)==current_pos_head:
                    valid=True

    if valid:
        new_current_pos_tail=current_pos_tail
    else:
        dx,dy=1,1
        if xx==x and yy==y:
            dx,dy=0,0
        elif xx==x and yy!=y:
            dx=0
            dy*=(yy-y)//abs(y-yy)
        elif yy==y and xx!=x:
            dy=0 
            dx*=(xx-x)//abs(x-xx) 
        else:
            dx*=(xx-x)//abs(x-xx) 
            dy*=(yy-y)//abs(y-yy)
        new_current_pos_tail=(x+dx,y+dy)
        
    return new_current_pos_tail

def move_record_tail(move,nummove, current_pos_head,current_pos_tail,all_pos_tail):
    x,y=current_pos_head
    for i in range(int(nummove)):
        if "D" in move:
            y+=1
        elif "U" in move:
            y-=1
        elif "R" in move:
            x+=1
        elif "L" in move:
            x-=1
        
        current_pos_head=(x,y)
        current_pos_tail=move_tail(current_pos_tail,current_pos_head)
        all_pos_tail.append(current_pos_tail)
        
    return current_pos_head,current_pos_tail

def print_grid(l):
    minx=min([x for x,y in l])
    maxx=max([x for x,y in l])
    miny=min([y for x,y in l])
    maxy=max([y for x,y in l])
    for j in range(miny,maxy+1):
        st=""
        for i in range(minx,maxx+1):
            if (i,j) in l :
                st+="#"
            elif (i,j)==(0,0):
                st+="s"
            else:
                st+="."
        print(st)
def part1and2(lines):
    d=dict()
    x,y=0,0
    current_pos_tail=(x,y)
    current_pos_head=current_pos_tail
    all_pos_tail=[current_pos_tail]
    for line in lines :
        move,nummove= line.split(" ")
        current_pos_head,current_pos_tail=move_record_tail(move,nummove,current_pos_head,current_pos_tail,all_pos_tail)
    #print_grid(set(all_pos_tail))
    
    retour1 = len(set(all_pos_tail))
    
    for _ in range(8):
        current_pos_tail=(0,0)
        all_pos_tai2=[current_pos_tail]
        for pos in all_pos_tail:
            current_pos_tail=move_tail(current_pos_tail, pos)
            all_pos_tai2.append(current_pos_tail)
        all_pos_tail=all_pos_tai2
    return retour1, len(set(all_pos_tail))
    
print(part1and2(lines))