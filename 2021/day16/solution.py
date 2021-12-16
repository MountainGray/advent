inp = open('2021/day16/input.txt').read()
htb = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
ns = []
for char in inp:
    ns.append(htb[char])

ns = "".join(ns)
vn = []
def parse_packet(packet):
    ver = int(packet[:3],2)
    vn.append(ver)
    typ = int(packet[3:6],2)
    if typ ==4:
        i = 6
        lit = []
        while True:
            ns = packet[i:i+5]
            lit.append(ns[1:])
            if ns[0]=="0":
                break
            i+=5
        lit = int("".join(lit),2)
        return lit, i+5
    else:
        vals = []
        lti = packet[6]
        if lti == "0":
            section = 15
            total_length_in_bits = int(packet[7:7+section],2)
            i=0
            while i <total_length_in_bits:
                val, idx = parse_packet(packet[22+i:])
                i+=idx
                vals.append(val)
            return_len = 22+i

        else:
            section = 11
            num_subpackets = int(packet[7:7+section],2)
            i = 0
            for _ in range(num_subpackets):
                val, idx = parse_packet(packet[18+i:])
                i+=idx
                vals.append(val)
            
            return_len = 18+i
        
        if typ == 0:
            return sum(vals), return_len
        elif typ == 1:
            start = vals[0]
            for i in range(1, len(vals)):
                start *=vals[i]
            return start, return_len
        elif typ == 2:
            return min(vals), return_len
        elif typ == 3:
            return max(vals), return_len
        elif typ == 5:
            if vals[0]>vals[1]:
                return 1, return_len
            else:
                return 0, return_len
        elif typ == 6:
            if vals[0]<vals[1]:
                return 1, return_len
            else:
                return 0, return_len
        elif typ == 7:
            if vals[0]==vals[1]:
                return 1, return_len
            else:
                return 0, return_len




        




print(vn)
print(sum(vn))
print(parse_packet(ns))