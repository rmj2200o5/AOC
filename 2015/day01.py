with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day01in.txt") as ipt:
    data = ipt.read()

def part1():
    floor = 0
    for c in data:
        if c=="(":
            floor+=1
        else:
            floor-=1
    print(floor)
def part2():
    floor = 0
    for i in range(len(data)):
        if data[i]=="(":
            floor+=1
        else:
            floor-=1
            if floor<0:
                print(i+1)
                return
part2()
