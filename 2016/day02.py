
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day02in.txt") as ipt:
    steps = ipt.read().splitlines()

def part1():
    key = dict()
    for i in range(3):
        for j in range(3):
            key[(i,j)]=(i%3)*3+j+1
    last = (1,1)
    move = {"U":(-1,0),"R":(0,1),"D":(1,0),"L":(0,-1)}
    def getKey(steps,last):
        current = [x for x in last]
        for c in steps:
            current = [current[i]+move.get(c)[i] for i in range(2)]
            current = [i if i>=0 else 0 for i in current]
            current = [i if i<3 else 2 for i in current]
        return (current[0],current[1])

    for i in range(len(steps)):
        last = getKey(steps[i],last)
        print(key.get(last),end="")


def part2():
    key = dict()
    x = 1
    for i in range(3):
        for j in range(2-i,3+i):
            key[(i,j)] = x
            x+=1
    x = 65
    for i in range(3,5):
        for j in range(2-(4-i),3+(4-i)):
            key[(i,j)] = chr(x)
            x+=1
    # print(key)
    move = {"U":(-1,0),"R":(0,1),"D":(1,0),"L":(0,-1)}
    last = (2,0)
    def getKey(steps,last):
        current = [x for x in last]
        for c in steps:
            temp = current.copy()
            temp = [temp[i]+move.get(c)[i] for i in range(2)]
            t = (temp[0],temp[1])
            if t not in key:
                continue
            current = temp
        return (current[0],current[1])
    for i in range(len(steps)):
        last = getKey(steps[i],last)
        print(key.get(last),end="")

part1()
print()
part2()
