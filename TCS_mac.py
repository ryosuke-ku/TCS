import os
import subprocess, sys
import urllib.request as req
from bs4 import BeautifulSoup as bs4
from collections import defaultdict
import collections

inputcode = []
file = open('Nicad-5.0/projects/systems/a.java', 'w')
print('↓ Input Code ↓')
while True:
    x = input()
    inputcode.append(x)
    file.write(x.replace('\n', '') + '\n')
    if x == "":
        break

file.close()
for low in inputcode:
    print(low)

project_list = ['systems']
# for i in project_list:
#     file = open('NICAD/projects/' + i +'/a.java', 'w')
#     file.write(x)
#     file.close()

os.chdir('/Users/ryosuke/Desktop/TCS/Nicad-5.0')

print(os.getcwd())

cp = subprocess.run(['./nicad5','functions','java','projects/' + project_list[0] ,'default-report'])

os.chdir('/Users/ryosuke/Desktop/TCS')
print(os.getcwd())

# cp2 = subprocess.run(['python','scraping.py'])

