dots, folds= open('2021/day13/input.txt').read().split('\n\n')
dots = [list(map(int, pair.split(","))) for pair in dots.split("\n")]
folds = folds.replace("fold along ","").split("\n")
def folb(pos, idx, axis):
    offset = 1 if axis == 'y' else 0
    if pos[offset] > idx:
        pos[offset]= idx*2-pos[offset]
    return pos
for fold in folds:
    axis, num = fold.split("=")
    for i in range(len(dots)):
        dots[i] = folb(dots[i], int(num), axis)
for i in range(max(dots, key=lambda x: x[1])[1]+1):
    for j in range(max(dots, key=lambda x: x[0])[0]+1):
        if [j,i] in dots:
            print('#', end='')
        else:
            print('.', end='')
    print()
print()





    
