with open("day03in.txt","r") as f:
    trees = f.read().split("\n")

product = 1
right = [1,3,5,7,1]
down = [1,1,1,1,2]
for i in range(5):
    count = 0
    row = 0
    col = 0
    while row < len(trees):
        if col >= len(trees[row]):
            col -= len(trees[row])
        if trees[row][col] == "#":
            count += 1
        row += down[i]
        col += right[i]
    print(count)
    product*=count

print(product)