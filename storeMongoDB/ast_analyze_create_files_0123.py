import logging.config
from ast.ast_processor_Production import AstProcessorProduction
from ast.ast_processor_Production_line import AstProcessorProductionLine
from ast.ast_processor_Test_line import AstProcessorTestLine
from ast.ast_processor_Test import AstProcessorTest
from ast.ast_processor_TestMethodCall import AstProcessorTestMethodCall
from ast.basic_info_listener_pt import BasicInfoListener
import glob
import re
import os
from collections import defaultdict
import xlwt

from pymongo import MongoClient
from datetime import datetime


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

def printProductionPath(project_name):
    initTestPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\**\\*Test.java', recursive=True)
    productionPath1 =[]
    for initTestPath in initTestPath1:
        testProjectName = re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath)[re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath).find("\\") + 1:][:re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath)[re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath).find("\\") + 1:].find('\\')]
        # print(testProjectName)
        testFileName = initTestPath[initTestPath.rfind("\\") + 1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\' + testProjectName + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            productionPath1.append(prodPath1[0].replace('\\','/'))
    return productionPath1


def printTestPath(project_name):
    initTestPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\**\\*Test.java', recursive=True)
    testPath1 = []
    for initTestPath in initTestPath1:
        testProjectName = re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath)[re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath).find("\\") + 1:][:re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath)[re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\", "", initTestPath).find("\\") + 1:].find('\\')]
        # print(testProjectName)
        testFileName = initTestPath[initTestPath.rfind("\\") + 1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\' + testProjectName + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            testPath1.append(initTestPath.replace('\\','/'))
    return testPath1

def makeFolder():
    os.mkdir('projects')
    projects_array = ['0123','ABCD','EFGH','IJKL','MNOP','QRST','UVW','XYZ']
    # projects_array = ['0123']
    for project in projects_array:
        data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')
        # print(data_set_0123)
        os.mkdir('projects\\' + project)
        for project_data in data_set:
            num_slash = project_data.rfind("\\")
            project_folder = project_data[num_slash + 1:]
            print(project_folder)
            os.mkdir('projects\\' + project + '\\' + project_folder)
            os.mkdir('projects\\' + project + '\\' + project_folder + '\\main')
            # os.mkdir('projects\\' + project + '\\' + project_folder + '\\test')

def delete_emptyProjects():
    try:
        os.rmdir('projects\\0123\\')
    except OSError as e:
        print('catch OSError:', e)
        pass

def testMethodMapCall(Path):
    Testmethodcalls_list = AstProcessorTestMethodCall(None, BasicInfoListener()).execute(Path) #target_file_path(テストファイル)内のメソッド名をすべて取得
    testMethodMapcall = defaultdict(list)
    # num = 0
    for i in Testmethodcalls_list:
        for j in Testmethodcalls_list[i]:
            if len(j) == 0:
                pass
            else:
                testMethodMapcall[j] = i
    
    return testMethodMapcall


if __name__ == '__main__':
    # makeFolder()
    # x = 'D:/ryosuke-ku/data_set/Git_20161108/0123/0xCopy_RelaxFactory/RelaxFactory/rxf-core/src/main/java/rxf/core/Rfc822HeaderState.java'
    # Productionmethods_list = AstProcessorProduction(None, BasicInfoListener()).execute(x) #プロダクションファイル内のメソッド名をすべて取得
    # print(Productionmethods_list)
    # print(len(Productionmethods_list))

    # ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(x) #プロダクションファイル内のメソッド名をすべて取得
    # print(ProductionmethodLine_list)
    # print(len(ProductionmethodLine_list))

    y = 'D:/ryosuke-ku/data_set/Git_20161108/0123/0xCopy_RelaxFactory/RelaxFactory/rxf-couch/src/test/java/rxf/couch/Rfc822HeaderStateTest.java'
    # TestmethodLine_list = AstProcessorTestLine(None, BasicInfoListener()).execute(y) #プロダクションファイル内のメソッド名をすべて取得
    # print(TestmethodLine_list)

    Testmethodcalls_list = AstProcessorTestMethodCall(None, BasicInfoListener()).execute(y) #target_file_path(テストファイル)内のメソッド名をすべて取得
    # print(Testmethodcalls_list)

    # testDict = testMethodMapCall(y)
    # print(testDict)
    # rd = rdict(testDict)
    # print(remethods)

    # z = 'C:/Users/ryosuke-ku/Desktop/TCS/NICAD/projects/systems/NICAD_ant/Nicad_t1_ant1.java'

    # ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(z) #プロダクションファイル内のメソッド名をすべて取得
    # print(ProductionmethodLine_list)
    # print(len(ProductionmethodLine_list))


    clint = MongoClient()
    db = clint['testMapList']

    project = '0123'
    data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')

    for project_data in data_set:
        project_folder = project_data[project_data.rfind("\\") + 1:]
        # print(project_folder)
        # 00joshi_hqapp
        project_name = str(project) + '/' + project_folder
        # print(project_name)
        # 0123/00joshi_hqapp
        PPath = printProductionPath(project_name)
        TPath = printTestPath(project_name)

        num_projects = int(len(PPath))

        if len(PPath) != 0 and len(TPath) != 0:
            # print(project_folder)
            for num_path in range(num_projects):

                Productionmethods_list = AstProcessorProduction(None, BasicInfoListener()).execute(PPath[num_path]) #プロダクションファイル内のメソッド名をすべて取得
                ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(PPath[num_path]) #プロダクションファイル内のメソッド名をすべて取得
                TestmethodLine_list = AstProcessorTestLine(None, BasicInfoListener()).execute(TPath[num_path]) #プロダクションファイル内のメソッド名をすべて取得

                PPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", PPath[num_path])  # projectX/~/a.java
                TPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", TPath[num_path])  # projectX/~/aTest.java
        
                testDict = testMethodMapCall(TPath[num_path])
                # print(testDict)
                rd = rdict(testDict)

                # print(Productionmethods_list)

                file_num = 0
                for ProductionMethod in Productionmethods_list:
                    # print(ProductionMethod)
                    startline = int(ProductionmethodLine_list[ProductionMethod][0])-1
                    endline = int(ProductionmethodLine_list[ProductionMethod][1])
                    # print('start: ' + str(startline) + ' end: ' + str(endline))

                    PMethod = ProductionMethod[:ProductionMethod.find('_')]
                    # print(PMethod)
                    # PPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", PPath[num_path])  # projectX/~/a.java
                    # TPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", TPath[num_path])  # projectX/~/aTest.java
 
                    path_dir = PPath_last[:PPath_last.rfind('/')+1]
                    file_name = PPath_last[PPath_last.rfind('/')+1:][:PPath_last[PPath_last.rfind('/')+1:].rfind('.')]

                    f = open(PPath[num_path], "r", encoding="utf-8")
                    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                    f.close()

                    remethods = rd["^(?=.*" + PMethod + ").*$"]
                    rts = list(set(remethods))
                    if len(remethods) == 0:
                        pass
                    else:

                        os.makedirs('systems/' + path_dir, exist_ok=True)
                        file = open('systems/' + path_dir + file_name + '.java', "w")

                        print(str(startline) + '_' + str(endline) + ':' + 'systems/' + path_dir + file_name + '.java')
                        for line in range(len(lines)):
                            if line == 0:
                                file.write('public class ' + file_name.capitalize() + '{\n')
                            else:
                                file.write('\n')

                        file.close()
                        file = open('systems/' + path_dir + file_name + '.java', "r", encoding="utf-8")
                        file_lines = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)

                        for row in range(len(file_lines)):
                            # print(row)
                            if row >= startline and row <= endline:
                                file_lines[row] = lines[row].replace('\n', '') + '\n'
                        file.close()
                        # print(file_lines)

                        with open('systems/' + path_dir + file_name + '.java', 'w', encoding="utf-8") as f:
                            for file_line in file_lines:
                                f.write(file_line) 

                        file_num += 1

                        for rt in rts:
                            startline_test = int(TestmethodLine_list[rt][0])-1
                            endline_test = int(TestmethodLine_list[rt][1])

                            post = {
                                'path': PPath_last,
                                'startline1': startline,
                                'endline1': endline,
                                'testpath': TPath_last,
                                'startline2': startline_test,
                                'endline2': endline_test,
                            }
                            db.testMap_0123.insert_one(post)  
                    
                     



    # clint = MongoClient()
    # db = clint['testList']

    # project = '0123'
    # data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')
    
    
    # for project_data in data_set:
    #     project_folder = project_data[project_data.rfind("\\") + 1:]
    #     # print(project_folder)
    #     # 00joshi_hqapp
    #     project_name = str(project) + '/' + project_folder
    #     # print(project_name)
    #     # 0123/00joshi_hqapp
    #     PPath = printProductionPath(project_name)
    #     TPath = printTestPath(project_name)

     
    #     num_projects = int(len(PPath))
    #     if len(PPath) != 0 and len(TPath) != 0:
    #         # print(project_folder)
    #         for num in range(num_projects):

    #             Productionmethods_list = AstProcessorProduction(None, BasicInfoListener()).execute(PPath[num]) #プロダクションファイル内のメソッド名をすべて取得
    #             print(PPath[num])
    #             print(Productionmethods_list)
    #             ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(PPath[num]) #プロダクションファイル内のメソッド名をすべて取得
    #             print(ProductionmethodLine_list)
    #             TestmethodLine_list = AstProcessorTestLine(None, BasicInfoListener()).execute(TPath[num]) #プロダクションファイル内のメソッド名をすべて取得
    #             print(TestmethodLine_list)

    #             PPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", PPath[num])  # projectX/~/a.java
    #             TPath_last = re.sub(r"D:/ryosuke-ku/data_set/Git_20161108/0123/", "", TPath[num])  # projectX/~/aTest.java
    #             print(PPath_last)
    #             print(TPath_last)
    #             testDict = testMethodMapCall(TPath[num])
    #             # print(testDict)

    #             rd = rdict(testDict)    

    #             file_num = 0
    #             for ProductionMethod in Productionmethods_list:
    #                 print(ProductionMethod)
    #                 PMethod = ProductionMethod[:ProductionMethod.find('_')]
    #                 print(PMethod)
    #                 remethods = rd["^(?=.*" + PMethod + ").*$"]
    #                 rts = list(set(remethods))
    #                 if len(remethods) == 0:
    #                     pass
    #                 else:
    #                     startline = int(ProductionmethodLine_list[ProductionMethod][0])-1
    #                     endline = int(ProductionmethodLine_list[ProductionMethod][1])

    #                     # print(PPath[num])
    #                     f = open(PPath[num], "r", encoding="utf-8")
    #                     lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    #                     f.close()
    #                     path_dir = PPath_last[:PPath_last.rfind('/')+1]
    #                     file_name = PPath_last[PPath_last.rfind('/')+1:][:PPath_last[PPath_last.rfind('/')+1:].rfind('.')]
    #                     # print('path_dir:' + path_dir)
    #                     # print('file_name:' + file_name)
    #                     os.makedirs('systems/' + path_dir, exist_ok=True)
    #                     file = open('systems/' + path_dir + file_name + '_' + str(file_num) + '.java', "w")
                        
    #                     for line in range(len(lines)):
    #                         file.write('\n')

    #                     file.close()
    #                     file = open('systems/' + path_dir + file_name + '_' + str(file_num) + '.java', "r", encoding="utf-8")
    #                     file_lines = file.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)

    #                     for row in range(len(file_lines)):
    #                         # print(row)
    #                         if row >= startline and row <= endline:
    #                             file_lines[row] = lines[row].replace('\n', '') + '\n'
    #                     file.close()
    #                     # print(file_lines)

    #                     with open('systems/' + path_dir + file_name + '_' + str(file_num) + '.java', 'w', encoding="utf-8") as f:
    #                         for file_line in file_lines:
    #                             f.write(file_line)
                        
    #                     file_num += 1


    #                     for rt in rts:

    #                         startline_test = int(TestmethodLine_list[rt][0])-1
    #                         endline_test = int(TestmethodLine_list[rt][1])

    #                         post = {
    #                             'path': PPath_last,
    #                             'startline1': startline,
    #                             'endline1': endline,
    #                             'testpath': TPath_last,
    #                             'startline2': startline_test,
    #                             'endline2': endline_test,
    #                         }
    #                         db.testList.insert_one(post)  

       
