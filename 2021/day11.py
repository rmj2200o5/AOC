with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day11in.txt") as ipt:
    data = ipt.read().splitlines()
grid = []
for line in data:
    grid.append([int(i) for i in line])

# Idea 1
# Create a pendingFlash() method that checks if a 10+ is present
def printGrid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end=" ")
        print()
    print()
def allFlashed():
    for row in grid:
        for i in row:
            if i>0:
                return False
    return True
def pendingFlash():
    for row in grid:
        for i in row:
            if i>=10:
                return True
    return False
# Use Conway Method of traversing data
def conwaySearch():
    global grid
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            # Every time a position holds a 9, update all surrounding and set current to -1
            if grid[i][j]>=10:
                grid[i][j]=-1
                for k in range(max([0,i-1]), min([i+1,rows-1]) +1):
                    for l in range(max([0,j-1]), min([j+1,cols-1])+1):
                        # if any position holds a -1, it is not updated, since it has already flashed
                        if grid[k][l]==-1:
                            continue
                        grid[k][l]+=1
flashCount = 0
for x in range(1000):
    print("This is step",x)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j]+=1
    # printGrid()
    # Continue looping the Conway search until pendingFlash returns False
    while pendingFlash():
        conwaySearch()
    # at this point, all -1 are counted and set to 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==-1:
                grid[i][j]=0
                flashCount+=1
    if allFlashed():
        print("All Flash on Step",x+1)
        printGrid()
        break
print(flashCount)