from advent import get_input, solution_timer, submit
from collections import Counter

inp = get_input(2022, 3)
print(inp[0])
ans = 0

# priority a->z = 1->26
# priority A->Z = 27->52
def priority(a):
    return ord(a) - 64 +26 if a.isupper() else ord(a) - 96
print(priority('a'), priority('A'), priority('z'), priority('Z'))

#for i in inp:
    ## divide into two
    #a = i[:len(i)//2]
    #b = i[len(i)//2:]
    #for j in a:
        #if j in b:
            #ans += priority(j)
            #break

# for every three values
for i in range(0,len(inp),3):
    a = inp[i]
    b = inp[(i+1)]
    c = inp[(i+2)]
    for j in a:
        if j in b and j in c:
            ans += priority(j)
            break


submit(2022, 3,2, ans)




#@solution_timer(2022, 3, 1)
#def part_one(inp):
    #return 0

#@solution_timer(2022, 3, 2)
#def part_two(inp):
    #return 0

            
#if __name__ == "__main__":
    #input = get_input(2022, 3)
    #part_one(input)
    #part_two(input)