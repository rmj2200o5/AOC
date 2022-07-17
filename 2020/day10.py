ipt = open("day10in.txt")
data = ipt.read().split("\n")
ratings = [int(num) for num in data]
ratings.sort()
differences = [0,0,1]
differences[ratings[0]-1]+=1

for i in range(len(ratings)-1):
    diff = ratings[i+1]-ratings[i]
    differences[diff-1]+=1
print(ratings)

groupings4 = 0
groupings3 = 0
currentGroup = 1
options = 1
ratings.insert(0,0)
ratings.append(ratings[-1]+3)
for i in range(len(ratings)-1):
    if ratings[i]+1==ratings[i+1]:
        currentGroup+=1
    elif currentGroup==5:
        print(currentGroup)
        options*=7
        currentGroup = 1
    elif currentGroup==4:
        print(currentGroup)
        options*=4
        currentGroup = 1
    elif currentGroup==3:
        options*=2
        print(currentGroup)
        currentGroup = 1
    else:
        print(currentGroup)
        currentGroup = 1
print(options)