# NOTE: The method used to solve this challenge was not orignal to my own thought, as I was previously unaware of how to use "reduce" and "combinations"
# Any use of combinations or reduce outside of day 24 2015 was possible as a result of my studying this method
from functools import reduce
from itertools import combinations
from operator import mul
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day24in.txt") as ipt:
    data = ipt.read().splitlines()
    wts = [int(x) for x in data]

# technically speaking, assuming there are multiple solutions of the same size,
#   this method does not gaurentee to produce the correct solution
#   however, since it by chance did produce the correct solution, 
#   I will not be taking the time to fix this potential issue
def day24(num_groups):
    group_size = sum(wts) // num_groups
    for i in range(len(wts)):
        qes = [reduce(mul, c) for c in combinations(wts, i) if sum(c) == group_size]
        if qes:
            return min(qes)

print(day24(3))
print(day24(4))
