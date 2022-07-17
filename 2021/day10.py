from inspect import stack

with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day10in.txt") as ipt:
    lines = ipt.read().splitlines()

score = {")":3,"]":57,"}":1197,">":25137}
totalScore = 0
incomplete = []
for line in lines:
    match = {"(":")","[":"]","{":"}","<":">"}
    stk = []
    done = False
    for c in line:
        if done:
            break
        if c in match.keys():
            stk.append(c)
        else:
            if match.get(stk[-1:][0])==c:
                stk = stk[:-1]
            else:
                # print(stk[])
                totalScore+=score.get(c)
                done = True
    if not done:
        incomplete.append(stk[::-1])

totalScore2 = []
score = {"(":1,"[":2,"{":3,"<":4}
for line in incomplete:
    s = 0
    for c in line:
        s*=5
        s+=score.get(c)
    totalScore2.append(s)
totalScore2 = sorted(totalScore2)
print(len(totalScore2))
print(totalScore2[27])
