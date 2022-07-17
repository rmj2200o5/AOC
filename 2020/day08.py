ipt = open("day08in.txt")
#splits input into lines and stores in an array
commands = ipt.read().split("\n")
ipt.close()

def bootCode (i):
    changeCount = i
    count = 0
    index = 0
    accumulator = 0
    usedIndices = []
    while index < len(commands):
        reverse = False
        if index in usedIndices:
            return 0
        usedIndices.append(index)
        if changeCount == count:
            reverse = True
        cmd = commands[index].split()
        sign = cmd[1][0]
        # checks which command is used
        if reverse:
            if cmd[0] == "acc":
                # adds or subtracts from totalCoin
                if sign == "+":
                    accumulator += int(cmd[1][1:])
                else:
                    accumulator -= int(cmd[1][1:])
                index += 1
            elif cmd[0] == "jmp":
                index += 1
            else:
                if sign == "+":
                    index += int(cmd[1][1:])
                else:
                    index -= int(cmd[1][1:])
            reverse = False
        else:
            if cmd[0] == "acc":
                # adds or subtracts from totalCoin
                if sign == "+":
                    accumulator += int(cmd[1][1:])
                else:
                    accumulator -= int(cmd[1][1:])
                index += 1
            elif cmd[0] == "jmp":
                # adds or subtraction from current index
                if sign == "+":
                    index += int(cmd[1][1:])
                else:
                    index -= int(cmd[1][1:])
            else:
                index += 1
        count+=1

    return accumulator
found = False
i = 0
while not found:
    ans = bootCode(i)
    print(i)
    if ans!=0:
        found = True
        print(ans)
    i+=1
