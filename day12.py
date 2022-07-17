with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day12in.txt") as ipt:
    data = ipt.read().splitlines()
Cave = {}
for line in data:
    path = line.split("-")
    if path[0] not in Cave.keys():
        Cave[path[0]]=[path[1]]
    else:
        Cave.get(path[0]).append(path[1])
    if path[1] not in Cave.keys():
        Cave[path[1]]=[path[0]]
    else:
        Cave.get(path[1]).append(path[0])
def countPaths(currentCave, pastCave, noEntry):
    if currentCave=="start":
        return 1
    count = 0
    paths = Cave.get(currentCave)[:]
    paths = [path for path in paths if path not in noEntry]
    if len(paths)==0:
        return 0
    if currentCave[0]!=currentCave[0].upper():
        noEntry = noEntry+[currentCave]
    for path in paths:
        count+=countPaths(path,currentCave,noEntry)
    return count
print(countPaths("end",None,[]))
