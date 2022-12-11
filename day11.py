with open('data/my_input/11.in') as f:
    lines = [  line.strip() for line in f]
from operator import mul
from functools import reduce
import re

regnum=lambda x: re.findall(r'-?\d+',x)

class Monkey():

    def __init__(self,num,items,function,testfunction,num_true,num_false,monkeys,intnumdiv):
        self.num=num
        self.items=items
        self.function=function
        self.testfunction=testfunction
        self.num_true=num_true
        self.num_false=num_false
        self.monkeys=monkeys
        self.count=0
        self.intnumdiv=intnumdiv

    def send_item(self,item,num_monky,dmonkeys):
        dmonkeys[num_monky].items.append(item)
    def inspect_item(self):
        if self.items:
            item=self.items[0]
            self.items=self.items[1:]
            new_item=self.function(item) % reduce(mul,[m.intnumdiv for _,m in self.monkeys.items()])

            # print(item,self.function,new_item)
            # print(self.testfunction(new_item))
            if self.testfunction(new_item):
                # print("True send to",self.num_true)
                self.send_item(new_item,self.num_true,self.monkeys)
            else:
                # print("False send to",self.num_false)
                self.send_item(new_item,self.num_false,self.monkeys)
            self.count+=1

    def inspect_all_items(self):
        for _ in range(len(self.items)):
            self.inspect_item()               


def part1and2(lines):
    i=0
    dmonkeys=dict()
    items=[]
    function=lambda x:x
    testfunction=lambda x:x
    num_true=0
    num_false=0
    for l in lines :
        if "items" in l:
            items=list(map(int,regnum(l)))
        elif "Operation" in l :
            function= eval("lambda old : " + l.split("=")[1])
        elif "Test" in l :
            numdiv=regnum(l)[0]
            testfunction=eval("lambda x:x% {} ==0".format(numdiv))
        elif "true" in l:
            num_true=int(regnum(l)[0])
        elif "false" in l:
            num_false=int(regnum(l)[0])      
        elif l=="":
            dmonkeys[i]=Monkey(i,items,function,testfunction,num_true,num_false,dmonkeys,int(numdiv))
            items=[]
            function=lambda x:x
            testfunction=lambda x:x
            num_true=0
            num_false=0
            i+=1
    dmonkeys[i]=Monkey(i,items,function,testfunction,num_true,num_false,dmonkeys,int(numdiv))

    for j in range(1,10001):
        for i in range(len(dmonkeys)):
            dmonkeys[i].inspect_all_items()
    for i in range(len(dmonkeys)):
        print(dmonkeys[i].items)
    print(reduce(mul,sorted([m.count for _,m in dmonkeys.items()])[-2:]))
print(part1and2(lines))