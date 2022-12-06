import re
with open('data/my_input/5.in') as f:
    lines = [  line.strip() for line in f]

num=lambda x : re.findall(r'\d+',x)

# [T]     [Q]             [S]        
# [R]     [M]             [L] [V] [G]
# [D] [V] [V]             [Q] [N] [C]
# [H] [T] [S] [C]         [V] [D] [Z]
# [Q] [J] [D] [M]     [Z] [C] [M] [F]
# [N] [B] [H] [N] [B] [W] [N] [J] [M]
# [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
# [B] [W] [N] [P] [D] [V] [G] [L] [T]
#  1   2   3   4   5   6   7   8   9 


def part1and2(lines,part1):
    l1=['B','P','N','Q','H','D','R','T']
    l2=['W','G','B','J','T','V']
    l3=['N','R','H','D','S','V','M','Q']
    l4=['P','Z','N','M','C']
    l5=['D','Z','B']
    l6=['V','C','W','Z']
    l7=['G','Z','N','C','V','Q','L','S']
    l8=['L','G','J','M','D','N','V']
    l9=['T','P','M','F','Z','C','G']
    lis=[]
    lis.append([])
    lis.append(l1)
    lis.append(l2)
    lis.append(l3)
    lis.append(l4)
    lis.append(l5)
    lis.append(l6)
    lis.append(l7)
    lis.append(l8)
    lis.append(l9)
    for line in lines:
        l=num(line)
        if len(l)==3:
            move,froms,to=list(map(int,l))
            to_add,remain = lis[froms][len(lis[froms])-move:] ,lis[froms][:len(lis[froms])-move] 
            if part1:
                to_add.reverse()
            lis[to]=lis[to]+to_add
            lis[froms]=remain
    print("".join([l[-1] for l in lis if l]))
    return 0

part1and2(lines,True)
part1and2(lines,False)