ipt = open("day02in.txt")
depth = 0
dist = 0
aim = 0
data = ipt.read().split("\n")

for line in data:
    info = line.split(" ")
    cmd = info[0]
    num = int(info[1])
    if cmd=="forward":
        depth-=num*aim
        dist+=num
    elif cmd=="down":
        aim-=num
    elif cmd=="up":
        aim+=num
print(f"{depth} {dist}")
print(depth*dist)