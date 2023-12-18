import re

with open(r"C:\Users\Robert J\VS Code\PythonWorks\AdventOfCode\2023\day02in.txt".replace("\\","/")) as ipt:
    data = ipt.readlines()

#Part 1
maxRed = 12
maxGreen = 13
maxBlue = 14
IDSum = 0
for line in data:
    info = line.split(": ")
    gameNumber = int(re.findall(r"Game (\d+)",info[0])[0])
    # print(gameNumber)
    pulls = info[1].split("; ")

    colorCounts = {"red": 0, "green":0, "blue": 0}

    for pull in pulls:
        colors = re.findall(r"(\d+) (red|green|blue)", pull)
        # print(colors)
        for color in colors:
            if(int(color[0])>colorCounts[color[1]]):
                colorCounts[color[1]] = int(color[0])
    condition = colorCounts["red"]<=maxRed and colorCounts["green"]<=maxGreen and colorCounts["blue"]<=maxBlue
    IDSum+= gameNumber if condition else 0
print(IDSum)

#Part 2
from functools import reduce
totalPower = 0
for line in data:
    info = line.split(": ")
    gameNumber = int(re.findall(r"Game (\d+)",info[0])[0]) 
    # print(gameNumber)
    pulls = info[1].split("; ")

    colorCounts = {"red": 0, "green":0, "blue": 0}

    for pull in pulls:
        colors = re.findall(r"(\d+) (red|green|blue)", pull)
        # print(colors)
        for color in colors:
            if(int(color[0])>colorCounts[color[1]]):
                colorCounts[color[1]] = int(color[0])
    # print(colorCounts.values())
    totalPower+= reduce(lambda a, b: a*b, list(colorCounts.values())) # == colorCounts[red]*colorCounts[green]*colorCounts[blue]
print(totalPower)
