with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day06in.txt") as ipt:
    data = ipt.read().splitlines()

# Part 1
# on = set()
# def turnOn(x1,y1,x2,y2):
#     global on
#     for i in range(x1,x2+1):
#         for j in range(y1,y2+1):
#             on.add((i,j))
# def turnOff(x1,y1,x2,y2):
#     global on
    # for i in range(x1,x2+1):
    #     for j in range(y1,y2+1):
#             if (i,j) in on:
#                 on.remove((i,j))
# def toggle(x1,y1,x2,y2):
#     global on
#     for i in range(x1,x2+1):
#         for j in range(y1,y2+1):
#             if (i,j) in on:
#                 on.remove((i,j))
#             else:
#                 on.add((i,j))

# for line in data:
#     if "on" in line:
#         points = line[8:].split(" through ")
#         x1,y1 = [int(p) for p in points[0].split(",")]
#         x2,y2 = [int(p) for p in points[1].split(",")]
#         turnOn(x1,y1,x2,y2)
#     elif "off" in line:
#         points = line[9:].split(" through ")
#         x1,y1 = [int(p) for p in points[0].split(",")]
#         x2,y2 = [int(p) for p in points[1].split(",")]
#         turnOff(x1,y1,x2,y2)
#     else:
#         points = line[7:].split(" through ")
#         x1,y1 = [int(p) for p in points[0].split(",")]
#         x2,y2 = [int(p) for p in points[1].split(",")]
#         toggle(x1,y1,x2,y2)
# print(len(on))

# Part 2
on = {}
def turnOn(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i,j) in on:
                on[(i,j)]+=1
            else:
                on[(i,j)]=1
def turnOff(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i,j) in on:
                on[(i,j)]-=1
                if on.get((i,j))==0:
                    on.pop((i,j))
def toggle(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if (i,j) in on:
                on[(i,j)]+=2
            else:
                on[(i,j)]=2

for line in data:
    if "on" in line:
        points = line[8:].split(" through ")
        x1,y1 = [int(p) for p in points[0].split(",")]
        x2,y2 = [int(p) for p in points[1].split(",")]
        turnOn(x1,y1,x2,y2)
    elif "off" in line:
        points = line[9:].split(" through ")
        x1,y1 = [int(p) for p in points[0].split(",")]
        x2,y2 = [int(p) for p in points[1].split(",")]
        turnOff(x1,y1,x2,y2)
    else:
        points = line[7:].split(" through ")
        x1,y1 = [int(p) for p in points[0].split(",")]
        x2,y2 = [int(p) for p in points[1].split(",")]
        toggle(x1,y1,x2,y2)
print(sum(on.values()))
            
            