with open("day01in.txt","r") as f:
    strings = f.read().split("\n")
nums = [int(num) for num in strings]
print(nums)
found = False
for i in range(len(nums)):
    if found:
        break
    for j in range(i+1,len(nums)):
        if found:
            break
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==2020:
                found = True
                print(nums[i]*nums[j]*nums[k])
                break