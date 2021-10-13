import hashlib
inp = open('2015/day04/input.txt').read().split('\n')

# Need to actually implement md5 hash function :(

def md5_imported(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
# Part 1
def md5_hash(key):
    x = 0
    while True:
        hsh = md5_imported(key+str(x))
        if hsh[:5] == '00000': 
            return x
        else:
            x += 1

print("P1:",md5_hash(inp[0]))
# Part 2    
def md5_p2(key):
    x = 0
    while True:
        hsh = md5_imported(key+str(x))
        if hsh[:6] == '000000': 
            return x
        else:
            x += 1

print("P2:",md5_p2(inp[0]))