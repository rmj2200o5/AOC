count = 0
ipt = open("day01in.txt")
data = [int(num.strip()) for num in ipt.readlines()]
ipt.close()
sums = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2)]
for i in range(1,len(sums)):
    if sums[i]>sums[i-1]:
        count+=1
print(count)