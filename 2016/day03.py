import re
with open("C://Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day03in.txt") as ipt:
    data = ipt.read()
    triag = re.findall(r" *(\d+) *(\d+) *(\d+)",data)
    #extra searches for part2
    triag1 = re.findall(r" *(\d+) *\d+ *\d+\n *(\d+) *\d+ *\d+\n *(\d+) *\d+ *\d+",data)
    triag2 = re.findall(r" *\d+ *(\d+) *\d+\n *\d+ *(\d+) *\d+\n *\d+ *(\d+) *\d+",data)
    triag3 = re.findall(r" *\d+ *\d+ *(\d+)\n *\d+ *\d+ *(\d+)\n *\d+ *\d+ *(\d+)",data)
    triagP2 = triag1+triag2+triag3

def part1():
    count = 0
    for sides in triag:
        s = [int(x) for x in sides]
        sum = 0
        for x in s:
            sum+=x
        count += 1 if max(s) < sum - max(s) else 0
    print(count)


def part2():
    count = 0
    for sides in triagP2:
        s = [int(x) for x in sides]
        sum = 0
        for x in s:
            sum+=x
        count += 1 if max(s) < sum - max(s) else 0
    print(count)

part1()
part2()