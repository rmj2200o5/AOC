import re
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day23in.txt") as ipt:
    data = ipt.read()
    steps = re.findall(r"jmp \+\d+|inc \w+|tpl \w+|jmp -\d+|jie \w+, \+\d+|jio \w+, \+\d+",data)
    steps = data.splitlines()
a,b = 1,0

i = 0

while(i<46):
    s = steps[i]
    print(i,s)
    if "inc" in s:
        exec(f"{s[4]}+=1")
    elif "hlf" in s:
        exec(f"{s[4]}={s[4]}//2")
    elif "tpl" in s:
        exec(f"{s[4]}*=3")
    elif "jmp" in s:
        i+=int(s.split()[1])
        continue
    elif "jio" in s:
        if "a" in s and a==1:
            i+=int(s.split(", ")[1])
        elif "b" in s and b==1:
            i+=int(s.split(", ")[1])
        else:
            i+=1
        continue
    elif "jie" in s:
        if "a" in s and a%2==0:
            i+=int(s.split(", ")[1])
        elif "b" in s and b%2==0:
            i+=int(s.split(", ")[1])
        else:
            i+=1
        continue  
    i+=1
print(a,b)