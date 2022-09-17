# Can I use functools reduce to run the multiplication, division, and modulous on all items?


#write formula to derive index from position. use position to tell needed length of list
#   potential storage issues? List may be too long
# rows and columns are additive sequences
# 
from functools import reduce
from operator import mul

# arr = [20151125.0,0.0,0.0]
# ansr = [20151125]
# arr2 = reduce(lambda a,b : (a*252533)%33554393,arr)
# print(arr2)
# print((arr[0]*252533)%33554393)

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