ipt = open("day04in.txt")
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
info = []
count = 0
def containsAll(passport):
    start = [field[:3] for field in passport]
    # Goes through all fileds and check if they are present in the passport
    for field in fields:
        if not field in start and field!="cid":
            return False
    return True

#Checks conditions for all fields
def inRange(passport):
    start = [field[:3] for field in passport]
    #byr
    i = start.index("byr")
    byr = int(passport[i].split(":")[1])
    if byr<1920 or byr>2002:
        return False
    #iyr
    i = start.index("iyr")
    iyr = int(passport[i].split(":")[1])
    if iyr<2010 or iyr>2020:
        return False
    #eyr
    i = start.index("eyr")
    eyr = int(passport[i].split(":")[1])
    if eyr<2020 or eyr>2030:
        return False
    #hgt
    i = start.index("hgt")
    unit = passport[i][-2:]
    if unit != "cm" and unit!="in":
        return False
    else:
        hgt = int(passport[i].split(":")[1][:-2])
        if unit == "cm":
            if hgt < 150 or hgt > 193:
                return False
        elif hgt < 59 or hgt > 76:
            return False
    #hcl
    i = start.index("hcl")
    hcl = passport[i].split(":")[1]
    chars = ["0","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    if hcl[0] != "#" or len(hcl)!=7:
        return False
    for j in range(1,7):
        if not hcl[j] in chars:
            return False
    #ecl
    i = start.index("ecl")
    ecl = passport[i].split(":")[1]
    colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    if ecl not in colors:
        return False
    #pid
    i = start.index("pid")
    pid = passport[i].split(":")[1]
    if not pid.isdigit() or len(pid)!=9:
        return False
    return True

#iterate through all lines of input
for line in ipt:
    # New line character respresents the end of a passport
    if line == "\n":
        if containsAll(info) and inRange(info):
            # increase count if all fields were present, with the exception of cid
            count+=1
        #clears info array
        info = []
    else:
        #adds fields to info array
        info += line.split()
ipt.close()
#Call methods one more time
if containsAll(info) and inRange(info):
    count+=1
print(f"There are {count} valid passports")