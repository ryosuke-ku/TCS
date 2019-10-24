import glob
import os
import re


def printProductionPath(project_name):
    initTestPath1 = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\' + project_name + '\\**\\*Test.java', recursive=True)
    productionPath1 =[]
    for initTestPath in initTestPath1:
        testProjectName = re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath)[re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath).find("\\") + 1:][:re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath)[re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath).find("\\") + 1:].find('\\')]
        # print(testProjectName)
        testFileName = initTestPath[initTestPath.rfind("\\") + 1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\' + project_name + '\\' + testProjectName + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            productionPath1.append(prodPath1[0])
    return productionPath1

def printTestPath(project_name):
    initTestPath1 = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\' + project_name + '\\**\\*Test.java', recursive=True)
    testPath1 = []
    for initTestPath in initTestPath1:
        testProjectName = re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath)[re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath).find("\\") + 1:][:re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath)[re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\", "", initTestPath).find("\\") + 1:].find('\\')]
        # print(testProjectName)
        testFileName = initTestPath[initTestPath.rfind("\\") + 1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('C:\\Users\\ryosuke-ku\\Desktop\\' + project_name + '\\' + testProjectName + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            testPath1.append(initTestPath)
    return testPath1

if __name__ == '__main__':
    utility_allPath = printProductionPath('utility')

    for utility_path in utility_allPath:
        print(utility_path)
        f = open(utility_path, "r", encoding="utf-8")
        lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
        f.close()
        print(len(lines))
        utility_cut = re.sub(r"C:\\Users\\ryosuke-ku\\Desktop\\utility\\", "", utility_path)
        utility_dir = utility_cut[:utility_cut.rfind('\\')]

        print(utility_dir)
        os.makedirs('systems\\' + utility_dir, exist_ok=True)
        file = open('systems\\' + utility_cut,'w')
        for line in range(len(lines)):
            file.write('\n')