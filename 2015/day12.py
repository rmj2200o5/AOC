with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day12in.txt") as ipt:
    d = ipt.read()
data = [] # This line isn't necesarry...I just didn't know how to make the "data not defined" warning go away
exec("data = "+d)

def findSum(dat):
    if isinstance(dat,int):
        return dat
    if isinstance(dat,str):
        return 0
    sum = 0
    if isinstance(dat,list):
        for ob in dat:
            sum+=findSum(ob)
    if isinstance(dat,dict):
        for key in dat:
            sum+=findSum(dat.get(key))
    return sum

print(findSum(data))

def findSum2(dat):
    if isinstance(dat,int):
        return dat
    if isinstance(dat,str):
        return 0
    sum = 0
    if isinstance(dat,list):
        for ob in dat:
            sum+=findSum2(ob)
    if isinstance(dat,dict):
        tempSum = 0
        hasRed = False
        for key in dat:
            if dat.get(key) == "red":
                hasRed = True
                break
            tempSum+=findSum2(dat.get(key))
        if not hasRed:
            sum+=tempSum
    return sum

print(findSum2(data))
