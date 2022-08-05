import re
txt = "vzbxxzaa"

def increment(s,i):
    if ord(s[i])==122:
        return increment(s[:i]+"a"+s[i+1:],i-1)
    else: 
        return s[:i]+chr(ord(s[i])+1)+s[i+1:] 

def consec(s):
    i = 0
    while i<len(s)-2:
        if ord(s[i])+2 == ord(s[i+1])+1 and ord(s[i])+2 == ord(s[i+2]):
            return True
        i+=1
    return False

def goodPass(s):
    return not re.search(r"i|o|l",s) and re.search(r"(.)\1.*(.)\2",s) and consec(s)

while not goodPass(txt):
    txt = increment(txt,7)
print(txt)