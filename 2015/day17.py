with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day17in.txt") as ipt:
    sizes = [int(i) for i in ipt.read().splitlines()]

from itertools import combinations
def part1():
    count= 0
    for i in range(2,13):
        count+=len([i for i in combinations(sizes,i) if sum(i)==150])
    print(count)
def part2():
    count= 0
    for i in range(2,13):
        count+=len([i for i in combinations(sizes,i) if sum(i)==150])
        if count>0:
            print(count)
            return

part1()
part2()