ipt = open("day09in.txt")
data = [int(num) for num in ipt.read().splitlines()]
ipt.close()
prevNums = []
for i in range(25):
    prevNums.append(data[i])

invalidNum = 0
for num in data[25:]:
    found = False
    for i in range(len(prevNums)):
        if found:
            break
        for j in range(i,len(prevNums)):
            if prevNums[i]+prevNums[j] == num:
                found = True
                break
    if found:
        prevNums[0:1] = []
        prevNums.append(num)
        continue
    else:
        invalidNum = num
        print(num)
        break
finalFound = False
for size in range(2,len(data)+1):
    if finalFound:
        break
    for i in range(len(data)-size):
        slice = data[i:i+size]
        if sum(slice)==invalidNum:
            print(slice)
            print(min(slice)+max(slice))
            finalFound = True
            break

