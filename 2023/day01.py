import re
with open(r"C:\Users\Robert J\VS Code\PythonWorks\AdventOfCode\2023\day01in.txt".replace("\\","/")) as ipt:
    data = ipt.readlines()

# Part 1
sum = 0
for line in data:
    #Added the replace lines for Part 2
    line = line.replace("one","o1e")
    line = line.replace("two","t2o")
    line = line.replace("three","t3e")
    line = line.replace("four","4")
    line = line.replace("five","5e")
    line = line.replace("six","6")
    line = line.replace("seven","7n")
    line = line.replace("eight","e8t")
    line = line.replace("nine","n9e")
    digits = re.findall("\d", line)
    if(len(digits)>0):
        sum += int(digits[0])*10 + int(digits[-1])
print(sum)
