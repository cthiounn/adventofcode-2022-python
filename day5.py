import re
with open('data/my_input/5.in') as f:
    lines = [  line.strip() for line in f]

num=lambda x : re.findall(r'\d+',x)

#         [G]         [D]     [Q]    
# [P]     [T]         [L] [M] [Z]    
# [Z] [Z] [C]         [Z] [G] [W]    
# [M] [B] [F]         [P] [C] [H] [N]
# [T] [S] [R]     [H] [W] [R] [L] [W]
# [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
# [C] [N] [H] [R] [N] [H] [D] [J] [Q]
# [N] [D] [M] [G] [Z] [F] [W] [S] [S]


def part1and2(lines,part1):
    l1=['N','C','R','T','M','Z','P']
    l2=['D','N','T','S','B','Z']
    l3=['M','H','Q','R','F','C','T','G']
    l4=['G','R','Z']
    l5=['Z','N','R','H']
    l6=['F','H','S','W','P','Z','L','D']
    l7=['W','D','Z','R','C','G','M']
    l8=['S','J','F','L','H','W','Z','Q']
    l9=['S','Q','P','W','N']
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