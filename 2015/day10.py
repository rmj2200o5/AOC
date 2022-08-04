def lookAndSay(s):
    i = 0
    count = 0
    new = ""
    past = ""
    while i<len(s):
        if past == "":
            past = s[i]
            count = 1
        elif s[i] == past:
            count+=1
        else:
            new+=str(count)+past
            past = s[i]
            count = 1
        i+=1
    new+=str(count)+past
    return new

data = "1113122113"

print(data)
for i in range(50):
    data = lookAndSay(data)
print(len(data))
