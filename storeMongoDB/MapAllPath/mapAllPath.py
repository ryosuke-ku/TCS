import glob
import re
import os

initTestPath1 = glob.glob('C:/Users/ryosuke-ku/Desktop/NiCad-5.1/projects/ant/**/*Test.java', recursive=True)
intiTestPath2 = glob.glob('C:/Users/ryosuke-ku/Desktop/NiCad-5.1/projects/ant/**/Test*.java', recursive=True)

def lenAllTestPath():
    print(len(initTestPath1))

def printProductionPath():
    productionPath1 =[]
    for initTestPath in initTestPath1:
        # print(initTestPath)
        num = initTestPath.rfind("\\")
        testFileName = initTestPath[num+1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('C:/Users/ryosuke-ku/Desktop/NiCad-5.1/projects/ant/**/' + fileName , recursive=True)
        if len(prodPath1)==0:
            # print('None')
            pass
        else:
            # print(prodPath1[0])
            productionPath1.append(prodPath1[0])

    for printpath in productionPath1:
        print(printpath)


def printTestPath():
    testPath1 = []
    for initTestPath in initTestPath1:
        # print(initTestPath)
        num = initTestPath.rfind("\\")
        testFileName = initTestPath[num+1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('C:/Users/ryosuke-ku/Desktop/NiCad-5.1/projects/ant/**/' + fileName , recursive=True)
        if len(prodPath1)==0:
            # print('None')
            pass
        else:
            # print(prodPath1[0])
            testPath1.append(initTestPath)

    for printtestpath in testPath1:
        print(printtestpath)

printTestPath()
# printProductionPath()
# lenAllTestPath()