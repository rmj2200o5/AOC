# This solution is not currently functioning

with open("day07in.txt") as ipt:
    data = ipt.read().splitlines()
paths = {x.split(" -> ")[1]:x.split(" -> ")[0] for x in data}
def getSignal(w):
    if w.isdigit():
        # print(w)
        return int(w)
    wire = paths.get(w)
    print(f"{w}: {wire}")
    if "AND" in wire:
        w1,w2 = wire.split(" AND ")
        # print(w,wire)
        return getSignal(w1) & getSignal(w2)
    elif "OR" in wire:
        w1,w2 = wire.split(" OR ")
        # print(w,wire)
        return getSignal(w1) | getSignal(w2)
    elif "LSHIFT" in wire:
        w1,x = wire.split(" LSHIFT ")
        # print(w,wire)
        # print(f"w1: {w1}\twire:{wire}")
        return getSignal(w1)<<int(x)
    elif "RSHIFT" in wire:
        w1,x = wire.split(" RSHIFT ")
        # print(w,wire)
        return getSignal(w1)>>int(x)
    elif "NOT" in wire:
        w1 = wire.split(" ")[1]
        print(w1)
        return ~getSignal(w1)
    else:
        # print(w,wire)
        return getSignal(wire)
print(getSignal("a"))
