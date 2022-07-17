from collections import Counter
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day06in.txt") as ipt:
    data = ipt.read().split(",")
originalCount = Counter(data)
def update(C):
    births = C[0]
    C = C[1:]+[0]
    C[6]+=births
    C[8]+=births
    return C
print(originalCount)
Count = [0]+[int(originalCount.get(str(i))) for i in range(1,6)]+[0,0,0]

for i in range(256):
    Count = update(Count)
print(sum(Count))
