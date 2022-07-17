with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day08in.txt") as ipt:
    data = [entry.split(" | ") for entry in ipt.read().splitlines()]
def part1():
    count = 0
    good = [2,4,3,7]
    for entry in [data[i][1] for i in range(len(data))]:
        output = entry.split(" ")
        for num in output:
            if len(num) in good:
                count+=1
    print(count)
def part2():
    sum = 0
    for entry in data:
        #Unscramble the wires
        pos = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
        nums = entry[0].split(" ")
        one = [num for num in nums if len(num)==2][0]
        pos.get(2).append(one[0])
        pos.get(2).append(one[1])
        pos.get(5).append(one[0])
        pos.get(5).append(one[1])
        four = [num for num in nums if len(num)==4][0]
        f = [c for c in four if c not in one]
        pos.get(1).append(f[0])
        pos.get(1).append(f[1])
        pos.get(3).append(f[0])
        pos.get(3).append(f[1])
        seven = [num for num in nums if len(num)==3][0]
        pos.get(0).append([c for c in seven if c not in one][0])
        five = [num for num in nums if len(num)==5 and pos.get(1)[0] in num and pos.get(1)[1] in num][0]
        f = [c for c in five if c not in four and c not in pos.get(0)][0]
        pos.get(6).append(f)
        three = [num for num in nums if len(num)==5 and pos.get(2)[0] in num and pos.get(2)[1] in num][0]
        p5 = [c for c in five if c in seven and c not in pos.get(0)][0]
        pos[5] = [p5]
        pos[2] = [c for c in pos.get(2) if c not in pos.get(5)]
        p3 = [c for c in three if c not in seven and c not in pos.get(6)][0]
        pos[3] = [p3]
        pos[1] = [c for c in pos.get(1) if c not in pos.get(3)]
        eight = [num for num in nums if len(num)==7][0]
        e = [c for c in eight if c not in four and c not in three]
        pos[4] = e
        for item in pos.items():
            pos[item[0]] = item[1][0]
        #reverse the dictionary
        decoder = {x[1]:x[0] for x in pos.items()}
        odds = [1,3,5,7,21,11,13]
        for i in range(7):
            decoder[pos.get(i)] = odds[i]
        #decode the numbers
        key = {54:"0",16:"1",47:"2",37:"3",26:"4",35:"5",56:"6",17:"7",61:"8",40:"9"}
        output = entry[1].split(" ")
        num = ""
        for o in output:
            s = 0
            for c in o:
                s+=decoder.get(c)
            num+=key.get(s)
        sum+=int(num)

    print(sum)



        
        
part2()