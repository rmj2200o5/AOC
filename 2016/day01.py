import re

with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day1in.txt") as ipt:
    directions = re.findall(r"(R|L)(\d+)",ipt.read())
move = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]} # 0=N 1=E 2=S 3=W

def part1():
    dir = 0
    cord = [0,0]
    for d in directions:
        if d[0]=="R":
            dir = (dir+1)%4
        else:
            dir = (dir-+1)%4
        x = int(d[1])
        cord = [cord[i]+x*move.get(dir)[i] for i in range(2)]
    print(abs(cord[0])+abs(cord[1]))

def part2():
    positions = set()
    dir = 0
    cord = [0,0]
    for d in directions:
        if d[0]=="R":
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4
        x = int(d[1])
        for n in range(x):
            cord = [cord[i] + move.get(dir)[i] for i in range(2)]
            p = (cord[0],cord[1])
            if p in positions:
                print(f"Second Visit: {p}")
                print(abs(cord[0])+abs(cord[1]))
                return
            positions.add(p)
    print(abs(cord[0])+abs(cord[1]))
part1()
part2()
    
