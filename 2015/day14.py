import re
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day14in.txt") as ipt:
    data = ipt.read().splitlines()
    reindeer = {}
    # Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
    for dat in data:
        name, speed, move, rest = re.findall(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",dat)[0]
        reindeer[name]= (int(speed),int(move),int(rest))
# 2503 seconds
distance = {}
for name in reindeer:
    speed, move,rest = reindeer.get(name)
    dist = speed*move * (2503//(rest+move))
    rem = 2503%(rest+move)
    if rem<=move:
        dist+=rem*speed
    else:
        dist+=move*speed
    distance[name] = dist

print(distance)
print(max(distance.values()))
# Part 2

points = {k:0 for k in reindeer}
time = 0
while time<2503:
    time+=1
    distance = {}
    for name in reindeer:
        speed, move,rest = reindeer.get(name)
        dist = speed*move * (time//(rest+move))
        rem = time%(rest+move)
        if rem<=move:
            dist+=rem*speed
        else:
            dist+=move*speed
        distance[name] = dist
    max_key = max(distance, key=distance.get)
    points[max_key]+=1
print(max(points.values()))