with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day08in.txt") as ipt:
    strings = ipt.read().splitlines()
memoryLength = 0
literalLength = 0
for s in strings:
    memoryLength+=len(s)
    s = s.replace("\\\\","#").replace("\\\"","\"")
    while "\\x" in s:
        i = s.index("\\x")
        code = s[i:i+4]
        s = s.replace(code,chr(int(code[2:],16)))
    s = s.replace("#","\\")[1:-1]
    literalLength+=len(s)
print(memoryLength-literalLength)

memoryLength = 0
literalLength = 0
for s in strings:
    literalLength+=len(s)
    s = "\""+s.replace("\"","#\"").replace("\\","##").replace("#","\\")+"\""
    memoryLength+=len(s)
print(memoryLength-literalLength)