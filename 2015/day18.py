with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day18in.txt") as ipt:
    data = ipt.read().splitlines()
    grid = []
    for row in data:
        r = []
        for c in row:
            r.append(c)
        grid.append(r)
rows = len(grid[0])
cols = len(grid)
def runGen(grid):
    gcopy = []
    for r in grid:
        gcopy.append(r[:])
    for i in range(cols):
        for j in range(rows):
            on = 0
            if grid[i][j]=="!":
                continue
            for k in range(max(0,i-1),min(i+1,rows-1)+1):
                for l in range(max(0,j-1),min(j+1,cols-1)+1):
                    if i==k and j==l:
                        continue
                    if grid[k][l] == "#" or grid[k][l]=="!":
                        on+=1
            # print(on,end = " ")
            if on == 3:
                gcopy[i][j] = "#"
            elif on==2 and grid[i][j]=="#":
                gcopy[i][j] = "#" #redudant line
            else:
                gcopy[i][j]="."
        # print()
    return gcopy

def printGrid(g):
    for row in g:
        for c in row:
            print(c,end="")
        print()
    print()
def countLights(g):
    count = 0
    for row in g:
        for c in row:
            if c=="#" or c=="!":
                count+=1
    return count
for i in range(100):
    grid = runGen(grid)
print(countLights(grid))


