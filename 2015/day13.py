import re
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day13in.txt") as ipt:
    data = ipt.read().splitlines()
    names = []
    effects = {}
    for dat in data:
        num =  int(re.findall(r"[0-9]+",dat)[0])
        gl =  re.findall(r"lose|gain",dat)[0]
        if gl == "lose":
            num = num*-1
        n1 = re.findall(r"\A[a-zA-Z]* ",dat)[0][:-1]
        n2 = re.findall(r"[a-zA-Z]*\.",dat)[0][:-1]
        if n1 not in names:
            names.append(n1)
        if n2 not in names:
            names.append(n2)
        effects[n1+"-"+n2] = num
happiest = 0
def seating(current,remaining,path):
    r = [c for c in remaining if c != current]
    if len(r)==0:
        global happiest
        happiness = 0
        path = path+[current]
        for i in range(len(path)):
            happiness+=effects.get(str(path[i-1])+"-"+str(path[i]))
            happiness+=effects.get(str(path[i])+"-"+str(path[i-1]))
        if happiness>happiest:
            happiest = happiness
    for person in r:
        seating(person,r,path+[current])
for n in names:
    seating(n,[name for name in names if name != n],[])
print(happiest)

#Part 2 
happiest = 0
for n in names:
    effects[n+"-Me"] = 0
    effects["Me-"+n] = 0
names.append("Me")
for n in names:
    seating(n,[name for name in names if name != n],[])
print(happiest)