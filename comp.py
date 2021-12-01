import requests
import sys
import os

cookie  = open("credentials.txt", "r").read().split("\n")[0]
headers = {'session': cookie}
day, year = int(sys.argv[0]), 2021
url = f'https://adventofcode.com/{year}/day/{day}/input'
session = requests.Session()
resp = session.get(url,cookies=headers)
daypath = f'{year}/day{day:02}'
os.makedirs(daypath)
in_file = open(f'day{day:02}.txt','w')
in_file.write(resp.text)
in_file.close()
in_file = open(f'{year}/day{day:02}/solution.py','w')
in_file.write(f"inp = open('{year}/day{day:02}/input.txt').read().split('\\n')")
in_file.close()