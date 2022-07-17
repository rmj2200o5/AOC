with open("day05in.txt","r") as f:
    passports = f.read().split("\n")
IDs = []
for k in range(len(passports)):
    passport = passports[k]
    rowMin = 0
    rowMax = 127
    row = 0
    for i in range(6):
        if passport[i] == "F":
            rowMax = (rowMin + rowMax) // 2
        else:
            rowMin = (rowMin + rowMax) // 2+1
    if (passport[6]) == "F":
        row = rowMin
    else:
        row = rowMax
    colMin = 0
    colMax = 7
    col = 0
    for i in range(2):
        i+=7
        if passport[i] == "L":
            colMax = (colMin + colMax) // 2
        else:
            colMin = (colMin + colMax) // 2+1
    if passport[9]=="L":
        col = colMin
    else:
        col = colMax
    IDs.append(row*8+col)
IDs.sort()
for i in range(len(IDs)-1):
    if IDs[i]+1==IDs[i+1]-1:
        print(IDs[i]+1)
        break




