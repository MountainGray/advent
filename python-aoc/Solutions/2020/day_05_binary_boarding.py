inp = open('2020/day05/input.txt').read().split('\n')[:-1]
cords = [(x[:-3], x[-3:])for x in inp]
seat_ids = []
maxid=0
for row, col in cords:
    row_num = int(row.replace("F","0").replace("B","1"), 2)
    col_num= int(col.replace("L","0").replace("R","1"), 2)
    seatid = row_num * 8 + col_num
    seat_ids.append(seatid)
    maxid = max(maxid, seatid)
print("P1",maxid)

for x in range(min(seat_ids), maxid):
    if x not in seat_ids:
        print("P2:", x)
