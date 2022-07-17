with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day07in.txt") as ipt:
    data = [int(i) for i in ipt.read().split(",")]
# Sum of Consecutive Additive Series
def findGas(d):
    return (d+1)*d/2
High = max(data)
Low = min(data)
Gas = [0]*High
for crab in data:
    for i in range(High):
        Gas[i]+=findGas(abs(crab-i))
print(min(Gas))