def mostCommon(lst, index):
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for entry in lst:
        for i in range(len(entry)):
            if entry[i] == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1
    if zeroes[index] > ones[index]:
        return "0"
    else:
        return "1"


def leastCommon(lst, index):
    ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for entry in lst:
        for i in range(len(entry)):
            if entry[i] == "0":
                zeroes[i] += 1
            else:
                ones[i] += 1
    if zeroes[index] > ones[index]:
        return "1"
    else:
        return "0"


def filterList(lst,keep,index):
    return [num for num in lst if num[index]==keep]

ipt = open("day03in.txt")
data = ipt.read().split("\n")
datacopy = data.copy()

s = "10001"
i = 0
while len(datacopy)>1:
    datacopy = filterList(datacopy,mostCommon(datacopy,i),i)
    i+=1

print(int(datacopy[0],2))
ox = int(datacopy[0],2)
datacopy = data.copy()
i=0
while len(datacopy)>1:
    datacopy = filterList(datacopy,leastCommon(datacopy,i),i)
    i+=1
print(int(datacopy[0],2))
co = int(datacopy[0],2)

print(ox*co)

