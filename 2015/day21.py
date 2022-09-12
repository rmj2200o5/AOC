#Part 2 incorrect
import re
with open("C:/Users/Robert J/VS code/PythonWorks/AdventOfCode/2015/day21in.txt") as ipt:
    sW, sA, sR = ipt.read().split("\n\n")
weapons = re.findall(r"(\w+) +(\d+) *(\d+) *(\d+)",sW)
armors = re.findall(r"(\w+) +(\d+) *(\d+) *(\d+)",sA)
rings = re.findall(r"(\w+ \+\d) +(\d+) *(\d+) *(\d+)",sR)
rings = sorted(rings,key = lambda x:int(x[1]))

#Just try every combination of armor: Can do iteratively

#adding null piece for every item type
weapons = [("null", "0", "0","0")] + weapons
armors = [("null", "0", "0","0")] + armors
rings = [("null +0", "0", "0","0")] + rings

#stats format [health,damage,armor]
def beatBoss(pStats):
    bossStats = [104,8,1]
    # print(f"Player Stat: {pStats}")
    # print(f"Boss Stats: {bossStats}")
    # print()
    turn = 0
    while True:
        if turn%2==0:
            #player turn
            # print("Player Turn")
            bossStats[0]-=max(1,pStats[1]-bossStats[2])
            if bossStats[0]<=0:
                return True
        else:
            #boss turn
            # print("Boss turn")
            pStats[0]-=max(1,bossStats[1]-pStats[2])
            if pStats[0]<=0:
                return False
        # print(f"Boss: {bossStats}")
        # print(f"Player: {pStats}")
        # print()
        turn+=1
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
                        if cost<bestPrice:
                            print(cost,damage,armor)
                            print(w,a,r1,r2)
                        bestPrice = min(cost,bestPrice)
    print(bestPrice)


def part2():
    worstPrice = 0
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
                        if cost>worstPrice:
                            print(cost,damage,armor)
                            print(w,a,r1,r2)
                        worstPrice = max(cost,worstPrice)
    print(worstPrice)
# part1()
part2()
