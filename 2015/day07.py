with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day07in.txt") as ipt:
    data = ipt.read().splitlines()
paths = {x.split(" -> ")[1]:x.split(" -> ")[0] for x in data}
copy = {x:paths.get(x) for x in paths}
# Part 1
def getSignal(w):
    if w.isdigit():
        return int(w)
    wire = paths.get(w)
    if isinstance(wire,int):
        return wire
    if "AND" in wire:
        w1,w2 = wire.split(" AND ")
        paths[w] = getSignal(w1) & getSignal(w2)
        return paths.get(w)
    elif "OR" in wire:
        w1,w2 = wire.split(" OR ")
        paths[w] = getSignal(w1) | getSignal(w2)
        return paths.get(w)
    elif "LSHIFT" in wire:
        w1,x = wire.split(" LSHIFT ")
        paths[w] = getSignal(w1)<<int(x)
        return paths.get(w)
    elif "RSHIFT" in wire:
        w1,x = wire.split(" RSHIFT ")
        paths[w] = getSignal(w1)>>int(x)
        return paths.get(w)
    elif "NOT" in wire:
        w1 = wire.split(" ")[1]
        xo = str(bin(getSignal(w1)))[2:]
        xo = "0"*(16-len(xo))+xo
        xi = "".join(["1" if i == "0" else "0" for i in xo ])
        paths[w] = int(xi,2)
        return paths.get(w)
    else:
        paths[w] = getSignal(wire)
        return paths.get(w)

part1Signal = getSignal("a")
print(part1Signal)

# Part 2
paths = copy
paths["b"] = part1Signal
part2Signal = getSignal("a")
print(part2Signal)
