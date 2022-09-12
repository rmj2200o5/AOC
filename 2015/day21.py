import re
import math
with open("C:/Users/Robert J/VS code/PythonWorks/AdventOfCode/2015/day21in.txt") as ipt:
    sW, sA, sR = ipt.read().split("\n\n")
weapons = re.findall(r"(\w+) +(\d+) *(\d+) *(\d+)",sW)
armors = re.findall(r"(\w+) +(\d+) *(\d+) *(\d+)",sA)
rings = re.findall(r"(\w+ \+\d) +(\d+) *(\d+) *(\d+)",sR)
rings = sorted(rings,key = lambda x:int(x[1]))

#Just try every combination of equipment: Can do iteratively

#adding null piece for armor and rings type
armors = [("null", "0", "0","0")] + armors
rings = [("null +0", "0", "0","0")] + rings

#stats format: [health,damage,armor]
def beatBoss(pStats):
    bossStats = [104,8,1]
    turn = 0
    return math.ceil(bossStats[0]/max(1,pStats[1]-bossStats[2]))<=math.ceil(pStats[0]/max(1,bossStats[1]-pStats[2]))

    
def part1():
    bestPrice = 0xFFFFFFFF
    #PROBLEM: User does not need every armor type to beat the boss
    #Solution: Add a null piece for every item type
    for w in weapons:
        for a in armors:
            for r1 in rings:
                for r2 in rings:
                    if r1==r2:
                        continue
                    cost,damage,armor = 0,0,0
                    cost+=  int(w[1])+int(a[1])+int(r1[1])+int(r2[1])
                    damage+=int(w[2])+int(a[2])+int(r1[2])+int(r2[2])
                    armor+= int(w[3])+int(a[3])+int(r1[3])+int(r2[3])
                    if beatBoss([100,damage,armor]):
                        bestPrice = min(cost,bestPrice)
    print(f"Part 1: {bestPrice}")

wins = []
def part2():
    worstPrice = -1
    #PROBLEM: User does not need every armor type to beat the boss
    #Solution: Add a null piece for every item type
    for w in weapons:
        for a in armors:
            for r1 in rings:
                for r2 in rings:
                    if r1==r2:
                        continue
                    cost,damage,armor = 0,0,0
                    cost+=  int(w[1])+int(a[1])+int(r1[1])+int(r2[1])
                    damage+=int(w[2])+int(a[2])+int(r1[2])+int(r2[2])
                    armor+= int(w[3])+int(a[3])+int(r1[3])+int(r2[3])
                    if not beatBoss([100,damage,armor]):
                        wins.append(cost)
                        worstPrice = max(cost,worstPrice)
    print(f"Part 2: {worstPrice}")
part1()
part2()
