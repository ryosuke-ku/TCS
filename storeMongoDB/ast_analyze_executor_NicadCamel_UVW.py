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
        num = initTestPath.rfind("\\")
        testFileName = initTestPath[num+1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            productionPath1.append(prodPath1[0])
    return productionPath1


def printTestPath(project_name):
    initTestPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\**\\*Test.java', recursive=True)
    testPath1 = []
    for initTestPath in initTestPath1:
        num = initTestPath.rfind("\\")
        testFileName = initTestPath[num+1:]
        fileName = testFileName.replace('Test','').replace('test','')
        prodPath1 = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project_name + '\\**\\' + fileName , recursive=True)
        if len(prodPath1)==0:
            pass
        else:
            testPath1.append(initTestPath)
    return testPath1


def storeToDB(project_num, projects_key, project_name):
    for numPath in range(project_num):
        print(numPath)
        print(TPath[numPath])
        Testmethodcalls_list = AstProcessorTestMethodCall(None, BasicInfoListener()).execute(TPath[numPath]) #target_file_path(テストファイル)内のメソッド名をすべて取得
        testMethodMapcall = defaultdict(list)
        num = 0
        for i in Testmethodcalls_list:
            for j in Testmethodcalls_list[i][0]:
                if len(j) == 0:
                    pass
                else:
                    testMethodMapcall[j + '_' + str(num)] = i
                    num += 1

        # print(testMethodMapcall)
        Productionmethods_list = AstProcessorProduction(None, BasicInfoListener()).execute(PPath[numPath]) #プロダクションファイル内のメソッド名をすべて取得
        print(numPath)
        print(PPath[numPath])

        number = 0
        for ProductionMethod in Productionmethods_list:
            rd = rdict(testMethodMapcall)
            remethods = rd["^(?=.*" + ProductionMethod + ").*$"]
            if len(remethods) == 0:
                pass
            else:
                print('----------------------------------------------------')
                print('key : ' + str(ProductionMethod))
                rt = list(set(remethods))
                print('value : ' + str(rt))
    
                for rtitem in rt:
                    post2 = {
                        'clone1': ProductionMethod,
                        'clone2': rtitem,
                    }
                    db.test.insert_one(post2)  
        
                file = open('projects\\' + projects_key + '\\' + project_name + '\\main\\' + str(number) + '.java','w') # Nicad_3.javaのファイルを開く
                ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(PPath[numPath]) #プロダクションファイル内のメソッド名をすべて取得
                print(ProductionmethodLine_list[ProductionMethod])
                startline = int(ProductionmethodLine_list[ProductionMethod][0])-1
                endline = int(ProductionmethodLine_list[ProductionMethod][1])
                f = open(PPath[numPath], "r", encoding="utf-8")
                lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                f.close()
                src = []
                print('<Production Code>')
                for x in range(startline,endline):
                    # print(lines2[x].replace('\n', ''))
                    srcLow = lines[x].replace('\n', '') + '\n'
                    print(srcLow)
                    file.write(srcLow)
                    src.append(srcLow)

                  
                file_test = open('projects\\' + projects_key + '\\' + project_name + '\\test\\' + str(number) + 'Test.java','w') # Nicad_3.javaのファイルを開く
                TestmethodLine_list = AstProcessorTestLine(None, BasicInfoListener()).execute(TPath[numPath]) #プロダクションファイル内のメソッド名をすべて取得
                # print(TestmethodLine_list)
                print(TestmethodLine_list[rtitem])
                startline_test = int(TestmethodLine_list[rtitem][0])-1
                endline_test = int(TestmethodLine_list[rtitem][1])
                f = open(TPath[numPath], "r", encoding="utf-8")
                lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                f.close()
                src_test = []
                print('<Test Code>')
                for x in range(startline_test,endline_test):
                    # print(lines2[x].replace('\n', ''))
                    srcLow = lines[x].replace('\n', '') + '\n'
                    print(srcLow)
                    file_test.write(srcLow)
                    src_test.append(srcLow)

                number += 1  


def makeFolder():
    os.mkdir('projects')
    # projects_array = ['1234','ABCD','EFGH','IJKL','MNOP','QRST','UVW','XYZ']
    projects_array = ['UVW']
    for project in projects_array:
        data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')
        # print(data_set_1234)
        os.mkdir('projects\\' + project)
        for project_data in data_set:
            num_slash = project_data.rfind("\\")
            project_folder = project_data[num_slash + 1:]
            print(project_folder)
            os.mkdir('projects\\' + project + '\\' + project_folder)
            os.mkdir('projects\\' + project + '\\' + project_folder + '\\main')
            os.mkdir('projects\\' + project + '\\' + project_folder + '\\test')

def dict_projectName():
    projectName = defaultdict(list)
    projects_array = ['UVW']
    for project in projects_array:
        data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')
        for project_data in data_set:
            num_slash = project_data.rfind("\\")
            project_folder = project_data[num_slash + 1:]
            # print(project_folder)
            projectName[project].append(project_folder)
    
    return projectName


if __name__ == '__main__':
    clint = MongoClient()
    db = clint['test']

    # a = printProductionPath('1234\\0xCopy_RelaxFactory')
    # print(a)
    # print(len(a))

    # b = printTestPath('1234\\0xCopy_RelaxFactory')
    # print(b)
    # print(len(b))

    projects_dic = dict_projectName()

    # for projects_key in projects_dic:
    #     print(projects_key)
    #     for projects_item in projects_dic[projects_key]:
    #         print(projects_item)

    for projects_key in projects_dic:
        print(projects_key)
        for projects_item in projects_dic[projects_key]:
            print(projects_item)
            project_num = len(projects_item)
            print(project_num)

            num_IndexError = 0
            num_UnicodeEncodeError = 0
            num_UnicodeDecodeError = 0
            num_RecursionError = 0
            num_FileNotFoundError = 0

            PPath = printProductionPath(projects_key + '\\' + projects_item)
            TPath = printTestPath(projects_key + '\\' + projects_item)
            if len(PPath) != 0 and len(TPath) != 0:
                print(PPath)
                print(TPath)
                try:
                    storeToDB(project_num, projects_key, projects_item)
                except IndexError as e:
                    print('catch IndexError:', e)
                    num_IndexError += 1
                except UnicodeEncodeError as e:
                    print('catch UnicodeEncodeError:', e)
                    num_UnicodeEncodeError += 1
                except UnicodeDecodeError as e:
                    print('catch UnicodeDecodeError:', e)
                    num_UnicodeDecodeError += 1
                except RecursionError as e:
                    print('catch RecursionError:', e)
                    num_RecursionError += 1
                except FileNotFoundError as e:
                    print('catch FileNotFoundError:', e)
                    num_FileNotFoundError += 1
                

    print('Number of IndexError :' + str(num_IndexError))
    print('Number of UnicodeEncodeError :' + str(num_UnicodeEncodeError))
    print('catch UnicodeDecodeError :' + str(num_UnicodeDecodeError))
    print('catch RecursionError :' + str(num_RecursionError))
    print('catch FileNotFoundError :' + str(num_FileNotFoundError))

