with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day02in.txt") as ipt:
    data = ipt.read().splitlines()
def part1():
    totalArea = 0
    for dimensions in data:
        l,w,h = [int(d) for d in dimensions.split("x")]
        a1,a2,a3 = 2*l*w,2*l*h,2*w*h
        totalArea+=a1+a2+a3+min([a1,a2,a3])//2
    print(totalArea)
def part2():
    ribbon = 0
    for dimensions in data:
        l,w,h = [int(d) for d in dimensions.split("x")]
        sides = [l,w,h]
        small = min(sides)
        big = max(sides)
        sides.remove(small)
        sides.remove(big)
        mid = sides[0]
        perimeter = 2*(small+mid)
        volume = l*w*h
        ribbon+=perimeter+volume
    print(ribbon)