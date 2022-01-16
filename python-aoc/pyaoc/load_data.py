"Utils for loading puzzle input"

def load(year,day, delimiter="\n", sub_delimiter=None, map_func=None):
    with open('input/{}/{}.txt'.format(year,day),'r') as f:
        if map_func & sub_delimiter :
            return [list(map(map_func, line.split(sub_delimiter))) for line in f.readlines()]
        elif sub_delimiter:
            return [line.split(sub_delimiter) for line in f.readlines()] 
        else:
            return f.read().split(delimiter)