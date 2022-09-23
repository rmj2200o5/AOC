from collections import Counter
with open("C://Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day06in.txt") as ipt:
    data = ipt.read().splitlines()

cS = [[],[],[],[],[],[],[],[]]

for msg in data:
    for i in range(len(msg)):
        cS[i].append(msg[i])

def part1():
    finalMsg = ""
    for i in range(8):
        finalMsg+= Counter(cS[i]).most_common()[0][0]
    print(finalMsg)

def part2():
    finalMsg = ""
    for i in range(8):
        finalMsg+= Counter(cS[i]).most_common()[::-1][0][0]
    print(finalMsg)
part1()
part2()