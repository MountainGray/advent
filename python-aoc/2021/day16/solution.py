inp = bin(int('1' + open("2021/day16/inp.txt").read(),16))[3:]  
def parse_packet(packet):
    ver = int(packet[:3],2)
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
        return lit, i+5, ver
    else:
        vals = []
        lti = packet[6]
        if lti == "0":
            section = 15
            total_length_in_bits = int(packet[7:7+section],2)
            i=0
            while i <total_length_in_bits:
                val, idx, vdx= parse_packet(packet[22+i:])
                i+=idx
                ver+=vdx
                vals.append(val)
            return_len = 22+i

        else:
            section = 11
            num_subpackets = int(packet[7:7+section],2)
            i = 0
            for _ in range(num_subpackets):
                val, idx, vdx = parse_packet(packet[18+i:])
                i+=idx
                ver += vdx
                vals.append(val)
            return_len = 18+i
        
        if typ == 0: return_val = sum(vals)
        elif typ == 1:
            start = 1
            for i in range(len(vals)):
                start *= vals[i]
            return_val = start
        elif typ == 2: return_val = min(vals)
        elif typ == 3: return_val = max(vals)
        elif typ == 5: return_val = 1 if vals[0]>vals[1] else 0
        elif typ == 6: return_val = 1 if vals[0]<vals[1] else 0
        else: return_val = 1 if vals[0]==vals[1] else 0
        return return_val, return_len, ver
print(parse_packet(inp)[::-2])