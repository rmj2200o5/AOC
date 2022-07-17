ipt  = open("day12in.txt")
instructions = ipt.read().split("\n")
x = 0
y = 0
Wx = 10
Wy = 1
for instruction in instructions:
    key = instruction[0]
    distance = int(instruction[1:])
    #N
    if key=="N" :
        Wy+=distance
    #E
    if key=="E":
        Wx+=distance
    #S
    if key=="S":
        Wy-=distance
    #W
    if key=="W":
        Wx-=distance
    #L
    if key=="L":
        direction = -(distance//90)%4
        xDif = Wx - x
        yDif = Wy - y
        for i in range(direction):
            temp = xDif
            xDif=yDif
            yDif=-temp
        Wx = x+xDif
        Wy = y+yDif


    #R
    if key == "R":
        direction = (distance // 90) % 4
        xDif = Wx - x
        yDif = Wy - y
        for i in range(direction):
            temp = xDif
            xDif = yDif
            yDif = -temp
        Wx = x + xDif
        Wy = y + yDif

    #F
    if key=="F":
        for i in range(distance):
            xDif = Wx - x
            yDif = Wy - y
            x = Wx
            y = Wy
            Wx = x + xDif
            Wy = y + yDif
    print(f"Ship({x}, {y}) Waypoint({Wx}, {Wy})")
print(f"Ship({x}, {y}) Waypoint({Wx}, {Wy})")
print(f"{abs(x)+abs(y)}")
