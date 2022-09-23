import re 
with open("C://Users/Robert J/VS Code/PythonWorks/AdventOfCode/2016/day07in.txt") as ipt:
    data = ipt.read().splitlines()

#Part 1
abba = [d for d in data if re.search(r"(\w)(\w)\2\1",d) and not re.search(r"\[\w*(\w)(\w)\2\1\w*\]",d) and d[re.search(r"(\w)(\w)\2\1",d).start()]!=d[re.search(r"(\w)(\w)\2\1",d).start()+1]]
print(len(abba))

#Part 2
tempaba = [d for d in data if re.search(r"(\w)(\w)\1[a-z\[\]]*\[[a-z]*\2\1\2[a-z]*\]",d) or re.search(r"\[[a-z]*(\w)(\w)\1[a-z]*\][a-z\[\]]*\2\1\2",d)]
aba = []
for d in tempaba:
    if re.search(r"(\w)(\w)\1[a-z\[\]]*\[[a-z]*\2\1\2[a-z]*\]",d) and d[re.search(r"(\w)(\w)\1[a-z\[\]]*\[[a-z]*\2\1\2[a-z]*\]",d).start()]!=d[re.search(r"(\w)(\w)\1[a-z\[\]]*\[[a-z]*\2\1\2[a-z]*\]",d).start()+1]:
        #check if aba is in []
        s = re.search(r"(\w)(\w)\1[a-z\[\]]*\[[a-z]*\2\1\2[a-z]*\]",d).start()
        b = False
        for i in [x for x in range(0,s)][::-1]:
            if d[i]=="]":
                break
            if d[i]=="[":
                b = True
                break
        if b :
            continue
        print("Type 1")
        aba.append(d)
    elif re.search(r"\[[a-z]*(\w)(\w)\1[a-z]*\][a-z\[\]]*\2\1\2",d) and d[re.search(r"\[[a-z]*(\w)(\w)\1[a-z]*\][a-z\[\]]*\2\1\2",d).end()-1]!=d[re.search(r"\[[a-z]*(\w)(\w)\1[a-z]*\][a-z\[\]]*\2\1\2",d).end()-2]:

        aba.append(d)

for ip in aba:
    rg = re.search(r"(\w+)(\w+)\1[a-z\[\]]*\2\1\2",ip).span()
    print(ip)
    rg = ip[rg[0]:rg[1]]
    s = rg[:3]+rg[-3:]
    print(s)
print(len(aba))
