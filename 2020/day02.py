with open("day02in.txt","r") as f:
    lines = f.read().split("\n")
validCount = 0
for line in lines:
    data = line.split()
    amount = data[0].split("-")
    first = int(amount[0])-1
    second = int(amount[1])-1
    char = data[1][0]
    password = data[2]
    if (password[first]==char or password[second]==char) and password[first]!=password[second]:
        validCount+=1

print(validCount)
