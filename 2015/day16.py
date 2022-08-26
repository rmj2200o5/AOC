import re
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day16in.txt") as ipt:
    data = ipt.read().splitlines()
    aunts = []
    for line in data:
        #Sue 500: cars: 1, perfumes: 6, vizslas: 1
        aunt = re.findall(r"\w+: \d+",line)
        aunts.append([(dat.split(":")[0],int(dat.split(": ")[1])) for dat in aunt])
        #[('cars', 1), ('perfumes', 6), ('vizslas', 1)]

key = {"children":3,"cats":7,"samoyeds":2,"pomeranians":3,"akitas":0,"vizslas":0,"goldfish":5,"trees":3,"cars":2,"perfumes":1}

for i in range(500):
    good = True
    for item in aunts[i]:
        if item[0]=="cats" or item[0]=="trees":
            good = good and item[1]>key.get(item[0])
        elif item[0]=="pomeranians" or item[0]=="goldfish":
            good = good and item[1]<key.get(item[0])
        else:
            good = good and item[1]==key.get(item[0])
    if good:
        print(f"Aunt {i+1} meets the requirements")
