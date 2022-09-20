import re
from collections import Counter
from functools import reduce
with open("C://Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day04in.txt") as ipt:
    data = ipt.read()
    rooms = re.findall(r"[a-z\-]+\d+\[\w+\]",data)

def realRoom(s):
    # print(s)
    checksum = re.findall(r"\[(\w+)\]",s)[0]
    # print(checksum)
    common = sorted(Counter(re.sub(r"-",r"",s[:-10])).most_common(),key = lambda x:(-x[1],ord(x[0])))[:5]
    for c in common:
        if c[0] not in checksum:
            # print(common)
            return False
    return True
def part1():
    real = [room for room in rooms if realRoom(room)]
    x = reduce(lambda a,b: a+int(re.findall(r"\d+",b)[0]),real,0)
    print(x)

real = [room for room in rooms if realRoom(room)]

def decrypt(room):
    s = re.sub(r"-",r" ",room[:-10])
    n = int(re.findall(r"\d+",room)[0])
    n = n%26
    newS = ""

    for c in s:
        if c==" ":
            newS+=" "
            continue
        x = chr((ord(c)-97+n)%26+97)
        newS+=x
    return newS

def part2():
    for room in real:
        s = decrypt(room)
        if s == "northpole object storage ":
            print(int(re.findall(r"\d+",room)[0]))
            break


part1()
part2()
