from collections import Counter
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day05in.txt") as fin:
    data = fin.read().splitlines()
# Part 1 - Horizontal and Vertical Lines

def part1():
    allPoints = []

    #Parse data
    for line in data:
        firstPoint, secondPoint = line.split(' -> ')
        x1, y1 = tuple(map(int,firstPoint.split(",")))
        x2, y2 = tuple(map(int,secondPoint.split(",")))
        
        # Only consider horizontal and vertical lines
        if x1==x2 or y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    allPoints.append((x,y))
    return len([point for point in Counter(allPoints).values() if point > 1])

def part2():
    allPoints = []

    #Parse data
    for line in data:
        firstPoint, secondPoint = line.split(' -> ')
        x1, y1 = tuple(map(int,firstPoint.split(",")))
        x2, y2 = tuple(map(int,secondPoint.split(",")))
        
        # Only consider horizontal and vertical lines
        if x1==x2 or y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    allPoints.append((x,y))
        else:
            x = x1
            y = y1
            xinc = 1 if x1<x2 else -1
            yinc = 1 if y1<y2 else -1
            while True:
                allPoints.append((x,y))
                if x==x2:
                    break
                x+=xinc
                y+=yinc
    return len([point for point in Counter(allPoints).values() if point > 1])


# print(f"The answer to part 1 as the following: {part1()}")
print(f"The answer to part 2 as the following: {part2()}")