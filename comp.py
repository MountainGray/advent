import requests
import sys
import os

cookie  = open("credentials.txt", "r").read().split("\n")[0]
headers = {'session': cookie}
day, year = int(sys.argv[1]), 2021
url = f'https://adventofcode.com/{year}/day/{day}/input'
session = requests.Session()
resp = session.get(url,cookies=headers)
daypath = f'{year}/day{day:02}'
in_file = open(f'{year}/day{day:02}/input.txt','w')
in_file.write(resp.text[:-1]) # get rid of newline at eof
in_file.close()