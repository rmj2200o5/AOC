ipt = open("day06in.txt")
data = ipt.read().split("\n")
sum = 0
count = 0
dict = {}
for line in data:
    if line != "":
        for char in line:
            if char in dict:
                dict[char] = dict.get(char)+1
            else:
                dict[char] = 1
        count+=1
    else:
        for char in dict:
            if dict[char]==count:
                sum+=1
        dict = {}
        count = 0
print(sum)
