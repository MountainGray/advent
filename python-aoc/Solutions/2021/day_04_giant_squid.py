inp = open('2021/day04/input.txt').read().split('\n\n')
nums = [int(i) for i in inp[0].split(",")]
boards = [[[int(i) for i in filter(lambda x: x!="",line.split(" "))]for line in board.split("\n")]for board in inp[1:]]

def checkboard(board, nums):
    for line in board:
        if set(line).issubset(nums):
            return True
    for i in range(len(board[0])):
        if set([line[i] for line in board]).issubset(nums):
            return True
    return False

def get_ans(board: list, nums: set, final):
    board_unrolled = set([item for sublist in board for item in sublist])
    leftover = board_unrolled - nums
    return sum(leftover)*final

#p1
bingo = False
idx = 0
while not bingo:
    called = set(nums[:idx+1])
    for board in boards:
        if checkboard(board, called):
            bingo = True
            print("P1:", get_ans(board, called, nums[idx]))
            break
    idx += 1
# p2
for idx in range(len(nums)):
    called = set(nums[:idx+1])
    for board in boards:
        if checkboard(board, called):
            boards.remove(board)
            if len(boards) == 0:
                print("P2:", get_ans(board, called, nums[idx]))
