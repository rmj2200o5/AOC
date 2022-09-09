ipt = 33100000
from functools import reduce

def factors1(n):    
    return [i for i in set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))]
def factors2(n):
    return [i for i in set(reduce(list.__add__,([n//i] for i in range(1, 51) if n % i == 0)))]
def numGifts(facts):
    n = 0
    for fact in facts:
        n+=10*fact
    return n

def part1():
    fSum = ipt//10
    x = 3
    while True:
        s = sum(factors1(x))
        if s>=fSum:
            break
        x+=3
    print(f"Part 1 Answer: {x}")
x = 100

def part2():
    fSum = ipt//11
    x = 3
    while True:
        s = sum(factors2(x))
        if s>=fSum:
            break
        x+=3
    print(f"Part 2 Answer: {x}")
part1()
part2()
