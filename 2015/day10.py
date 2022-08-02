#This solution is not functioning yet

data = "1113122113"
def lookAndSay(s,x):
    if x ==1:
        return str(len(s))+str(x)
    d = s.split(str(x))
    final = ""
    count = 0
    i = 0
    while i<len(d) and d[i]=="":
        i+=1
    if i>0:
        final+=str(i)+str(x)
    start = i
    while i<len(d):
        if d[i] == "":
            count+=1
        else:
            if i>start:
                final+=str(count+1)+str(x)
                count = 0
            final+=lookAndSay(d[i],x-1)
        i+=1
    if count>0:
        final+=str(count)+str(x)
    return final

# print(data)
for i in range(40):
    data = lookAndSay(data,3)
    # print(data)
    
print(len(data))
