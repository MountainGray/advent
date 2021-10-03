import requests
import sys
import os

cookie  = open("credentials.txt", "r").read().split("\n")[0]

headers = {'session': cookie}

#if len(sys.argv) != 3:
    #print('Wrong number of arguments')
    #exit(0)
if sys.argv[1] == 'load':
    day, year = int(sys.argv[2]), int(sys.argv[3])
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    session = requests.Session()
    resp = session.get(url,cookies=headers)

    in_file = open(f'day{day:02}.txt','w')
    in_file.write(resp.text)
    in_file.close()
elif sys.argv[1] == 'test':
    year = int(sys.argv[2])
    day = int(sys.argv[3])

    daypath = f'{year}/day{day:02}'
    os.makedirs(daypath)

    url = f'https://adventofcode.com/{year}/day/{day}/input'

    session = requests.Session()
    resp = session.get(url,cookies=headers)

    in_file = open(daypath + f'/input.txt','w')
    in_file.write(resp.text)
    in_file.close()

    in_file = open(daypath + f'/solution.py','w')
    in_file.write("inp = open('./input.txt').read().split('\\n')")
    in_file.close()

elif sys.argv[1] == 'full':
    for year in range(2015,2021):
        for day in range(1,26):

            daypath = f'{year}/day{day:02}'
            os.makedirs(daypath)

            url = f'https://adventofcode.com/{year}/day/{day}/input'

            session = requests.Session()
            resp = session.get(url,cookies=headers)

            in_file = open(daypath + f'/input.txt','w')
            in_file.write(resp.text)
            in_file.close()

            in_file = open(daypath + f'/solution.py','w')
            in_file.write(f"inp = open('{daypath}/input.txt').read().split('\\n')")
            in_file.close()

elif sys.argv[1] == 'adjust':
    for year in range(2015,2021):
        for day in range(1,26):
            in_file = open(f'{year}/day{day:02}/solution.py','w')
            in_file.write(f"inp = open('{year}/day{day:02}/input.txt').read().split('\\n')")
            in_file.close()

