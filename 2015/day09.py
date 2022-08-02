with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day09in.txt") as ipt:
    data = ipt.read().splitlines()
    cities = []
    distance = {dat.split(" = ")[0].replace(" to ","-"):int(dat.split(" = ")[1]) for dat in data}
    for dat in data:
        for city in  dat.split(" = ")[0].split(" to "):
            if city not in cities:
                cities.append(city)

shortest = 0xFFFFFFFF
longest = 0
def routes(current,remaining,dist,path):
    r = [c for c in remaining if c != current]
    if len(r) == 0:
        global shortest
        if dist<shortest:
            shortest = dist
        global longest
        if dist>longest:
            longest = dist
        return
    for city in r:
        d = distance.get(f"{current}-{city}")
        if d == None:
            d = distance.get(f"{city}-{current}")
        rem = [c for c in r if c != city]
        routes(city,r,dist+d,path+[current])

for city in cities:
    routes(city,[c for c in cities if c != city],0,[])
print(f"Part 1: {shortest}")
print(f"Part 2: {longest}")
