with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day09in.txt") as ipt:
    data = ipt.read().splitlines()

lows = []

rows = len(data)
cols = len(data[0])
sum = 0
for i in range(rows):
    for j in range(cols):
        found = False
        for k in range(max([0,i-1]), min([i+1,rows-1]) +1):
            if found:
                break
            for l in range(max([0,j-1]), min([j+1,cols-1])+1):
                if not (i==k or j==l):
                    continue
                if (i==k and j==l):
                    continue
                if  int(data[k][l]) <=int(data[i][j]):
                    found = True
        if not found:
            lows.append((i,j))
            sum+=int(data[i][j])+1
# print(sum)
#write a recursive method that checks the four directions around a given point
# cords is a list of coordinate tuples
# returns a list of all points
# create counted with the original point
def basinPoints(height,cords,counted):
    lows = [(cords[0]-1,cords[1]),(cords[0]+1,cords[1]),(cords[0],cords[1]-1),(cords[0],cords[1]+1)]
    # check for out of bounds in lows
    lows = [c for c in lows if c[0]>=0 and c[0]<len(data) and c[1]>=0 and c[1]<len(data[0])]
    for low in lows:
        if low not in counted and int(data[low[0]][low[1]])>height and int(data[low[0]][low[1]])<9:
            counted.append(low)
            basinPoints(int(data[low[0]][low[1]]),low,counted)
    return counted

# print(lows[0])
# print(basinPoints(int(data[lows[0][0]][lows[0][1]]),lows[0],[lows[0]]))
# print(len(basinPoints(int(data[lows[0][0]][lows[0][1]]),lows[0],[lows[0]])))
lengths = []
for low in lows:
    lengths.append(len(basinPoints(int(data[low[0]][low[1]]),low,[low])))
lengths = sorted(lengths)[::-1]
print(lengths)
print(lengths[0]*lengths[1]*lengths[2])
