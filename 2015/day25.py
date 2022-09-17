#Enter the code at row 2978, column 3083.
def getCount(row, column):
	return sum(range(row + column - 1)) + column

def getNext(num):
    return (num*252533)%33554393
x = 20151125.0
c = getCount(2978,3083)
print(c)
for i in range(c-1):
    x = getNext(x)
print(x)
