with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day03in.txt") as ipt:
    data = ipt.read()
x,y=0,0
points = {(0,0)}
key = {"<":-1,">":1,"v":-1,"^":1}
xs = "<>"
ys = "^v"

def part1():
    for c in data:
        if c in xs:
            x+=key.get(c)
        else:
            y+=key.get(c)
        p = (x,y)
        if p not in points:
            points.add(p)
    print(len(points))
    
xb,yb = 0,0
def part2():
    bot = False
    for c in data:
        if bot:
            bot = not bot
            if c in xs:
                xb+=key.get(c)
            else:
                yb+=key.get(c)
            p = (xb,yb)
            if p not in points:
                points.add(p)
        else:
            bot = not bot
            if c in xs:
                x+=key.get(c)
            else:
                y+=key.get(c)
            p = (x,y)
            if p not in points:
                points.add(p)
    print(len(points))
