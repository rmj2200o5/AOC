class Bingo:
    
    def __init__(self,nums):
        self.grid = [[],[],[],[],[]]
        for i in range(len(nums)):
            self.grid[i//5].append(nums[i])
        
        self.called = []
        for i in range(5):
            self.called.append([0,0,0,0,0])
    
    def checkBoard(self,num):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j]==num:
                    self.updateCalled(i,j)
                    return

    def updateCalled(self,row,col):
        self.called[row][col] = 1
    
    def isWon(self):
        for i in range(5):
            if "".join([str(n) for n in self.called[i]])=="11111":
                return True
            if self.called[0][i]+self.called[1][i]+self.called[2][i]+self.called[3][i]+self.called[4][i] == 5:
                return True
        return False
    
    def numUnmarked(self):
        sum = 0
        for i in range(25):
            if self.called[i//5][i%5] ==0:
                sum+=self.grid[i//5][i%5]
        return sum

    def __str__(self):
        out = ""
        for i in range(5):
            for j in range(5):
                out+=str(self.grid[i][j]) + " "
            out+="\n"
        return out

    @property
    def getCalled(self):
        out = ""
        for i in range(5):
            for j in range(5):
                out+=str(self.called[i][j]) + " "
            out+="\n"
        return out

        
        
        
    
    

# game1 = Bingo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
# print(game1.called)
# game1.checkBoard(1)
# print(game1.called)
# print(game1.isWon())
# for i in range(1,6):
#     game1.checkBoard(i*5+1)
# print(game1.called)
# print(game1.isWon())
# print(game1.numUnmarked())

ipt = open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2021/day04in.txt")
data = ipt.readlines()
boardList = []
draws = [int(i) for i in data[0].split(",")]
data = data[1:]
count = 0
boarddat = []
for row in data:
    if count==0:
        count=1
        boarddat = []
        continue
    for num in row.split(" "):
        if num=="":
            continue
        boarddat.append(int(num))
    count+=1
    if count==6:
        boardList.append(Bingo(boarddat))
        count = 0

found = False
bList = boardList[:]
for draw in draws:
    if found:
        break
    boardList = bList[:]
    for board in boardList:
        board.checkBoard(draw)
        if board.isWon():
            if len(boardList)==1:
                found = True
                print(boardList)
                print(draw)
                print(board.numUnmarked())
                print(draw*board.numUnmarked())
                print(board)
                print(board.getCalled)
                break
            bList.remove(board)
            
print("...did this break...")
    
