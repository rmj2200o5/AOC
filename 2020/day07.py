ipt = open("day07in.txt")
rules = ipt.read().split("\n")
ipt.close()
allColors = []
contents = []
numContents = []
for rule in rules:
    rule = rule[:-1]
    data = rule.split(" contain ")
    allColors.append(data[0][:-1])
    if data[1][0]=="n":
        numContents.append([])
        contents.append([])
        continue
    contains = data[1].split(", ")
    numColors = []
    color = []
    for c in contains:
        numColors.append(int(c[0]))
        if c[-1]=="s":
            color.append(c[2:-1])
        else:
            color.append(c[2:])
    numContents.append(numColors)
    contents.append(color)
'''print(allColors)
print(contents)
print(numContents)'''

def hasGold(i):
    colors = allColors[i]
    contains = contents[i]
    if "shiny gold bag" in contains:
        return True
    if len(contains)==0:
        return False
    for color in contains:
        j = allColors.index(color)
        if hasGold(j):
            return True
    return False
def numBags(i):
    contains = contents[i]
    numContains = numContents[i]
    if len(contains)==0:
        return 0
    num = sum(numContains)
    for j in range(len(contains)):
        color = contains[j]
        k = allColors.index(color)
        num += numBags(k)*numContains[j]
    return num
goldIndex = allColors.index("shiny gold bag")
print(numBags(goldIndex))

'''    
count=0
for i in range(len(allColors)):
    if hasGold(i):
        count+=1
print(count)'''


