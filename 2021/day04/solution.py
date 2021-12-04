inp = open('2021/day04/input.txt').read().split('\n')
nums= inp[0]
nums = [int(i) for i in nums.split(",")]

inp = open('2021/day04/input.txt').read().split('\n\n')
boards = inp[1:]

boards = [[[int(i) for i in filter(lambda x: x!="",line.split(" "))]for line in board.split("\n")]for board in boards]
def checkboard(board, nums):
    a = set(nums)
    for line in board:
        if set(line).issubset(a):
            return True
    for i in range(len(board[0])):
        if set([line[i] for line in board]).issubset(a):
            return True
    #if set([line[idx] for idx, line in enumerate(board)]).issubset(a):
        #return True
    #if set([line[-idx] for idx, line in enumerate(board)]).issubset(a):
        #return True
    return False

bboard = None
inb = None

solved = False
for idx in range(1,len(nums)):
    valid = nums[:idx+1]
    inb = nums[idx+1]
    iv = idx

    for board in boards:
        if checkboard(board, valid):
            boards.remove(board)
    if len(boards) == 1:
        board = boards[0]
        for idc in range(idx,len(nums)):
            valid = nums[:idc+1]
            if checkboard(board, valid):
                bboard = boards[0]
                inb = nums[idc]
                iv = idc+ 1
                break
        break   

boardnums = []
print(bboard)
for line in bboard:
    for i in line:
        boardnums.append(i)
leftover = set(boardnums) - set(nums[:iv])
print(nums[:inb+2])
print(leftover)
b = sum(leftover)
print(b)
print(inb)
print(b * inb)
