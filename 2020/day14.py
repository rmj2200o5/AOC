ipt = open("day14in.txt")
data = ipt.read().split("\n")
ipt.close()
mem = {}
mask = ""
def findInt(number):
    number = "".join(number)
    intNumber = 0
    for i in range(36):
        if number[i]=="1":
            intNumber+=2**(35-i)
    return intNumber
def findAddresses(memAddress):
    if not "X" in memAddress:
        return [findInt(memAddress)]
    i = memAddress.index("X")
    op1 = memAddress.copy()
    op2 = memAddress.copy()
    op1[i]="0"
    op2[i]="1"
    return findAddresses(op1)+findAddresses(op2)


for row in data:
    if row[:4]=="mask":
        mask = row[7:]
    else:
        info = row.split("=")
        address = info[0][4:-2]
        num = int(info[1][1:])
        biaddress = str(bin(int(address)))[2:]
        biaddress = "0"*(36-len(biaddress))+biaddress
        compAddress = []
        for i in range(36):
            if mask[i]=="X":
                compAddress.append(mask[i])
            elif mask[i]=="1" or biaddress[i]=="1":
                compAddress.append("1")
            else:
                compAddress.append("0")
        pAddresses = findAddresses(compAddress)
        for n in pAddresses:
            mem[n] = num
print(mem)
sum = 0
for item in mem:
    sum+=mem[item]
print(sum)
'''
for row in data:
    if row[:4]=="mask":
        mask = row[7:]
    else:
        info = row.split("=")
        address = info[0][4:-2]
        num = info[1][1:]
        binum = str(bin(int(num)))[2:]
        binum = "0"*(36-len(binum))+binum
        finNum = ""
        print(num)
        print(mask)
        print(binum)
        for i in range(36):
            if mask[i] != "X":
                finNum += mask[i]
            else:
                finNum += binum[i]
        finInt = 0
        print(finNum)
        for i in range(len(finNum)):
            if finNum[i] == "1":
                finInt += 2**(35-i)
        print(finInt)
        mem[address] = finInt
print(mem)
sum = 0
for item in mem:
    sum+=mem[item]
print(sum)
'''