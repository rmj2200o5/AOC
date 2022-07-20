import hashlib
search = "00000"
# key1 = "abcdef"
# num1 = "609043"
# string1 = key1+num1
# answer1 = str(hashlib.md5(string1.encode()).hexdigest())
# print(answer1[:5])

# key2 = "pqrstuv"
# num2 = "1048970"
# string2 = key2+num2
# answer2 = str(hashlib.md5(string2.encode()).hexdigest())
# print(answer2[:5])

def part1():
    input = "yzbqklnj"
    i = 0
    while True:
        string = input+str(i)
        answer = str(hashlib.md5(string.encode()).hexdigest())
        if answer[:5] == search:
            print(i)
            break
        i+=1
search = "000000"
def part2():
    input = "yzbqklnj"
    i = 0
    while True:
        string = input+str(i)
        answer = str(hashlib.md5(string.encode()).hexdigest())
        if answer[:6] == search:
            print(i)
            break
        i+=1