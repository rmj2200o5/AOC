import re
with open("C://Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day09in.txt") as ipt:
    file = ipt.read()

def part1(data):
    final = ""
    while re.search(r"(\d+x\d+)",data):
        r = re.search(r"(\d+x\d+)",data).span()
        final+=data[:r[0]-1]
        x1,x2 = [int(x) for x in data[r[0]:r[1]].split("x")]
        final+=data[r[1]+1:r[1]+1+x1]*x2
        data = data[r[1]+1+x1:]
    return final
print(len(part1(file)))
#returns length
def part2(data):
    if not re.search(r"(\d+x\d+)",data):
        return len(data)
    r = re.search(r"(\d+x\d+)",data).span()
    length=r[0]-1
    x1,x2 = [int(x) for x in data[r[0]:r[1]].split("x")]
    length+=x2*part2(data[r[1]+1:r[1]+1+x1])
    length+=part2(data[r[1]+1+x1:])
    return length
print(part2(file))