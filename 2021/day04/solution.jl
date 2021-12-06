inp = open(f-> read(f,String), "2021/day04/input.txt")
chunks = split(inp, "\n\n")
numbers = map(y->parse(Int,y), split(chunks[1], ","))
boards = [[[map(y-> parse(Int,y) ,split(line, " ", keepempty = false))] for line in split(board, "\n")] for board in chunks[2:end]]
println(numbers)
println(boards[1])
function chekboard(board, nums)
    for line in board
        if all(map(y-> contains(nums, y), line))
            return true
    end
    for i in range(1, len(board[1]))
        if all(map(y-> contains(nums, y), map(y-> y[i], board)))
            return true
        end
    end
end

function get
