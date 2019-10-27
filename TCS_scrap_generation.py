from urllib import request
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import shutil
import glob
import os
from collections import defaultdict

def writeHtml():
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('<style type="text/css">\n')
    file.write('body {font-family:Arial}\n')
    file.write('table {background-color:white; border:0px solid white; width:100%; margin-left:auto; margin-right: auto}\n')
    file.write('td {background-color:#ff7e75; padding:10px; border:0px solid white}\n')
    file.write('pre {background-color:white; padding:10px}\n')
    file.write('</style>\n')
    file.write('<title>Test Code Searcher Report</title>\n')
    file.write('<head>\n')
    file.write('<body>\n')
    file.write('<h2>Test Code Searcher Report</h2>\n')
    

#url
url = "file:///C:/Users/ryosuke-ku/Desktop/TCS/NICAD/projects/systems_functions-blind-clones/systems_functions-blind-clones-0.30-classes-withsource.html"

#get html
html = request.urlopen(url)

#set BueatifulSoup
soup = BeautifulSoup(html, "html.parser")

clint = MongoClient()
db = clint['testList']

codeArray = []
codePathArray = []

startLine = []
stopLine = []
codePathDict = defaultdict(list)

codePathClass = defaultdict(list)
srcCodeClass = defaultdict(list)

bodyCode = soup.find('body')


# クローンクラス<h3>の配列を作成し,類似コードが存在するファイルパス<td>を要素として配列に格納する処理
for item in bodyCode.find_all(['h3', 'td']):
    srcCodeArray = []
    if item.name == 'h3':
        key = item.text.replace('\n','').replace('\r','')
        print(key)
    if key and item.name == 'td':
        srccode = item.find('pre')
        srcCodeArray.append(srccode.text)
        # print(srccode.text)

        item.find('pre').decompose()
        path = item.text.replace('\n','').replace('\r','')
        print(path)
    
        codePathClass[path] = key
        srcCodeClass[path] = srcCodeArray
  
print(codePathClass)
for i in codePathClass:
    print(i)
    for j in codePathClass[i]:
        print(j)

# print(srcCodeClass)
# for i in srcCodeClass:
#     print(i)
#     for j in srcCodeClass[i]:
#         print(j)

# print('Class : ' + codePathClass['Lines 1 - 10 of projects/systems/a.java'])
# print(srcCodeClass[codePathClass['Lines 1 - 10 of projects/systems/a.java']])

# print(srcCodeClass[codePathClass['Lines 1 - 10 of projects/systems/a.java']])











# bodyCode = soup.find('body')
# for item in bodyCode.find_all(['h3', 'td']):
#     # print(item)
#     if item.name == 'h3':
#         h3 = item.text.replace('\n','').replace('\r','')
#         print(h3)

#         td = item.find_all('td')
#         print(td)
        # td_line = td.find('pre').decompose()
        # print(td_line)

    # if h3 and item.name == 'td':
    #     srccode = item.find('pre')
    #     print(srccode)
        # td = item.find('pre').decompose()
        # print(td)


# for h3 in tableCode.find_all('h3'):
#     print(h3)
#     for table in tableCode.find_all('table'):
#         for td in table.find_all('td'):
#             print(td)
#             td_line = td.find('pre').decompose()
#             print(td_line)
    


# num = 1
# for item in tableCode.find_all('table'):
#     print('table : ' + str(num))
#     num += 1
#     for td in item.find_all('td'):
#         print(td)
#         print('------------------------------------------------------------------')
    # print(item.find('td'))
    # print('-------------------------------------------------------------------------------------')
    # codeInfoArray = []
    # if item.name == 'td':
    #     srccode = item.find('pre')
    #     print(srccode)
    #     # codeInfoArray.append(srccode.text)
    #     item.find('pre').decompose()
    #     item_edited = item.text.replace('\n','')
    #     item_cut_edited = re.sub(r"Lines.*?projects/systems/", "", item_edited)
    #     # codeInfoArray.append(item_cut_edited)

    #     print(item_cut_edited)
        # codePath_cutFront = re.sub(r"Lines ", "", item_edited)
        # num = codePath_cutFront.find('o')
        # codePath_cutEnd = codePath_cutFront[:num]
        # codePath_rmSpace = codePath_cutEnd.replace(' ','')
        # num_hyphen = codePath_rmSpace.find('-')
        # startLine = int(codePath_rmSpace[:num_hyphen])-1
        # endLine = int(codePath_rmSpace[num_hyphen+1:])
        # codeInfoArray.append(startLine)
        # codeInfoArray.append(endLine)

#     codePathDict[item_cut_edited] = codeInfoArray

# print(codePathDict)

# tableCode = soup.find('table')
# for item in tableCode.find_all('td'):
#     codeInfoArray = []
#     if item.name == 'td':
#         srccode = item.find('pre')
#         codeInfoArray.append(srccode.text)
#         item.find('pre').decompose()
#         item_edited = item.text.replace('\n','')
#         item_cut_edited = re.sub(r"Lines.*?projects/systems/", "", item_edited)
#         codeInfoArray.append(item_cut_edited)

#         codePath_cutFront = re.sub(r"Lines ", "", item_edited)
#         num = codePath_cutFront.find('o')
#         codePath_cutEnd = codePath_cutFront[:num]
#         codePath_rmSpace = codePath_cutEnd.replace(' ','')
#         num_hyphen = codePath_rmSpace.find('-')
#         startLine = int(codePath_rmSpace[:num_hyphen])-1
#         endLine = int(codePath_rmSpace[num_hyphen+1:])
#         codeInfoArray.append(startLine)
#         codeInfoArray.append(endLine)

#     codePathDict[item_cut_edited] = codeInfoArray

# print(codePathDict)

# file = open('TCS_result.html','w')
# writeHtml()
# number = 0
# for key_path in codePathDict:
#     print(key_path)
#     if key_path != 'a.java':
#         print(codePathDict[key_path])
#         file.write('<TABLE BORDER="0">')
#         file.write('<h3>Clone Pairs ' + str(number) +'</h3>\n')
#         file.write('<TR>\n')
#         file.write('<TD>\n')
#         file.write('<table border="1" align="left" cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
#         file.write('<tr>\n')
#         file.write('<td>\n')
#         file.write('Input Code' + '\n')
#         file.write('<pre>\n')
#         file.write(codePathDict['a.java'][0][1:])
#         file.write('</pre>\n')
#         file.write('</td>\n')
#         file.write('</tr>\n')
#         file.write('</table>\n')
#         file.write('</TD>\n')
#         file.write('<TD>\n')
#         file.write('<table border="1"  cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
#         file.write('<tr>\n')
#         file.write('<td>\n')
#         file.write(codePathDict[key_path][1] + '\n')
#         file.write('<pre>\n')
#         file.write(codePathDict[key_path][0][1:])
#         file.write('</pre>\n')
#         file.write('</td>\n')
#         file.write('</tr>\n')
#         file.write('</table>\n')
#         file.write('</TD>\n')
#         file.write('</TR>\n')
#         file.write('</TABLE>\n')

#         items = db.testList.find({'startline1':int(codePathDict[key_path][2]),'endline1':int(codePathDict[key_path][3])})
        
#         for item in items:
#             testline_start = int(item['startline2'])
#             testine_end = int(item['endline2'])
#             testpath = item['testpath']
#             # print(testpath)
#             testpath_full = 'D:\\ryosuke-ku\\data_set\\Git_20161108\\utility\\' + testpath
#             f = open(testpath_full, "r", encoding="utf-8")
#             lines_origin = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
#             f.close()
#             print(testpath_full)
#             file.write('<table border="1" width="500" cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
#             file.write('<tr>\n')
#             file.write('<td>\n')
#             file.write(testpath + '\n')
#             file.write('<pre>\n')

#             for x in range(testline_start,testine_end):
#                 file.write(lines_origin[x].replace('\n', '') + '\n')

#             # file.write(item['testpath'] + '\n')
#             file.write('</pre>\n')
#             file.write('</td>\n')
#             file.write('</tr>\n')
#             file.write('</table>\n')
#             print(item)

#     number += 1

# # shutil.rmtree("C:Users\\ryosuke-ku\\Desktop\\TCS\\NICAD\\projects\\systems_functions-blind-clones")
# NICAD_functionPath_xml = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\TCS\\NICAD\\projects\\*.xml', recursive=True)
# for functionPath_xml in NICAD_functionPath_xml:
#     os.remove(functionPath_xml)

# NICAD_functionPath_log = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\TCS\\NICAD\\projects\\*.log', recursive=True)
# for functionPath_log in NICAD_functionPath_log:
#     os.remove(functionPath_log)