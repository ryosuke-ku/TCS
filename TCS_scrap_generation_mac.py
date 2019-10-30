from urllib import request
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient
import shutil
import glob
import os
from collections import defaultdict

class rdict(dict):
    def __getitem__(self, key):
        try:
            return super(rdict, self).__getitem__(key)
        except:
            try:
                ret=[]
                for i in self.keys():
                    m= re.match("^"+key+"$",i)
                    if m:ret.append( super(rdict, self).__getitem__(m.group(0)) )
            except:raise(KeyError(key))
        return ret


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
url = "file:///Users/ryosuke/Desktop/TCS/NiCad-5.0/projects/systems_functions-blind-clones/systems_functions-blind-clones-0.30-classes-withsource.html"

#get html
html = request.urlopen(url)

#set BueatifulSoup
soup = BeautifulSoup(html, "html.parser")

clint = MongoClient('163.221.190.202')
db = clint['testMapList']

codeArray = []
codePathArray = []

startLine = []
stopLine = []

bodyCode = soup.find('body')
print(bodyCode)

# クローンクラス<h3>の配列を作成し,類似コードが存在するファイルパス<td>を要素として配列に格納する処理

codePathArray = []
pathToClassDict = defaultdict(list)
classToPathsDict = defaultdict(list)
pathToFragmentDict = defaultdict(list)
pathToCodeInfoDict = defaultdict(list)

for item in bodyCode.find_all(['h3', 'table']):
    pathArray = []
    if item.name == 'h3':
        cloneclass = item.text.replace('\n','').replace('\r','')
        # print(cloneclass)

    if item.name == 'table':
        fragmentArray = []      
        tdInfo = item.find_all('td')
        for td in tdInfo:
            codeInfoArray = []
            fragment  = td.find('pre')
            fragmentArray.append(fragment.text)
            codeInfoArray.append(fragmentArray[0])
            td.find('pre').decompose()
            path = td.text.replace('\n','').replace('\r','')
            pathArray.append(path)

            formalPath = re.sub(r"Lines.*?projects/systems/", "", path)
            codeInfoArray.append(formalPath)
            # print(formalPath)
            path_front = re.sub(r"Lines ", "", path)
            path_line = path_front[:path_front.find('o')]
            path_rmSpace = path_line.replace(' ','')

            startLine = int(path_rmSpace[:path_rmSpace.find('-')])-1
            endLine = int(path_rmSpace[path_rmSpace.find('-')+1:])
            # print(str(startLine) + ':' + str(endLine))
            codeInfoArray.append(startLine)
            codeInfoArray.append(endLine)
            pathToCodeInfoDict[path] = codeInfoArray

            # print(codeInfoArray)

            pathToFragmentDict[path] = fragmentArray[0]
            # print(pathArray)
            pathToClassDict[path] = cloneclass

        classToPathsDict[cloneclass] = pathArray

rePathToClassDict = rdict(pathToClassDict)
classInfo = rePathToClassDict["^(?=.*" + 'projects/systems/a.java' + ").*$"]
print(classInfo[0])
pathInfos = classToPathsDict[classInfo[0]]
print(pathInfos)

rePathToCodeInfoDict = rdict(pathToCodeInfoDict)


for detected_path in pathInfos:
    if 'projects/systems/a.java' in detected_path:
        input_path = detected_path
        print(input_path)


file = open('TCS_result.html','w')
writeHtml()
clone_num = 1
for key_path in pathInfos:
    print(key_path)
    if 'projects/systems/a.java' not in key_path:
        print(key_path)
        file.write('<TABLE BORDER="0">')
        file.write('<h3>Clone Pairs ' + str(clone_num) +'</h3>\n')
        file.write('<TR>\n')
        file.write('<TD>\n')
        file.write('<table border="1" align="left" cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
        file.write('<tr>\n')
        file.write('<td>\n')
        file.write('Input Code' + '\n')
        file.write('<pre>\n')
        file.write(pathToCodeInfoDict[input_path][0][1:].replace('\n','') + '\n')
        file.write('</pre>\n')
        file.write('</td>\n')
        file.write('</tr>\n')
        file.write('</table>\n')
        file.write('</TD>\n')
        file.write('<TD>\n')
        file.write('<table border="1"  cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
        file.write('<tr>\n')
        file.write('<td>\n')
        file.write('Lines ' + str(pathToCodeInfoDict[key_path][2]) + ' - ' + str(pathToCodeInfoDict[key_path][3]) + ' of ' + pathToCodeInfoDict[key_path][1] + '\n')
        file.write('<pre>\n')
        file.write(pathToCodeInfoDict[key_path][0][1:].replace('\n','') + '\n')
        file.write('</pre>\n')
        file.write('</td>\n')
        file.write('</tr>\n')
        file.write('</table>\n')
        file.write('</TD>\n')
        file.write('</TR>\n')
        file.write('</TABLE>\n')

        items = db.mapingCollection.find({'path':pathToCodeInfoDict[key_path][1],'startline1':int(pathToCodeInfoDict[key_path][2]),'endline1':int(pathToCodeInfoDict[key_path][3])})
        
        for item in items:
            testline_start = int(item['startline2'])
            testine_end = int(item['endline2'])
            testpath = item['testpath']
            # print(testpath)
            testpath_full = '/Users/ryosuke/Desktop/TCS/0123/' + testpath
            f = open(testpath_full, "r", encoding="utf-8")
            lines_origin = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
            f.close()
            print(testpath_full)
            file.write('<table border="1" width="500" cellspacing="0" cellpadding="5" bordercolor="#333333">\n')
            file.write('<tr>\n')
            file.write('<td>\n')
            file.write('Lines ' + str(testline_start) + ' - ' + str(testine_end) + ' of ' + testpath + '\n')
            file.write('<pre>\n')

            for x in range(testline_start,testine_end):
                file.write(lines_origin[x].replace('\n', '') + '\n')

            # file.write(item['testpath'] + '\n')
            file.write('</pre>\n')
            file.write('</td>\n')
            file.write('</tr>\n')
            file.write('</table>\n')
            print(item)

    clone_num += 1

shutil.rmtree("/Users/ryosuke/Desktop/TCS/NiCad-5.0/projects/systems_functions-blind-clones")
NICAD_functionPath_xml = glob.glob('/Users/ryosuke/Desktop/TCS/NiCad-5.0/projects/*.xml', recursive=True)
print(NICAD_functionPath_xml)
for functionPath_xml in NICAD_functionPath_xml:
    os.remove(functionPath_xml)

NICAD_functionPath_log = glob.glob('/Users/ryosuke/Desktop/TCS/NiCad-5.0/projects/*.log', recursive=True)
for functionPath_log in NICAD_functionPath_log:
    os.remove(functionPath_log)
print(NICAD_functionPath_log)