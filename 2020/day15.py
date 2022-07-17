import time
start_time = time.time()
ipt = open("day15in.txt")
data = ipt.read().split(",")
ipt.close()
allNums = {}
for i in range(len(data)):
    allNums[int(data[i])]=i
i = len(data)
num = 0
while(i<29999999):
    if not num in allNums:
        allNums[num] = i
        num = 0
    else:
        n = allNums[num]
        allNums[num] = i
        num = i-n
    i+=1
print(num)
print(time.time()-start_time)