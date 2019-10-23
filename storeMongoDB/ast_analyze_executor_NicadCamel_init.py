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
        TPath_cutfront = re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\0123\\", "", TPath[numPath])
        TPath_last = TPath_cutfront.replace('\\','/')
        print(TPath_last)
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
        PPath_cutfront = re.sub(r"D:\\ryosuke-ku\\data_set\\Git_20161108\\0123\\", "", PPath[numPath])
        PPath_last = PPath_cutfront.replace('\\','/')
        print(PPath_last)
                
        ProductionmethodLine_list = AstProcessorProductionLine(None, BasicInfoListener()).execute(PPath[numPath]) #プロダクションファイル内のメソッド名をすべて取得
        TestmethodLine_list = AstProcessorTestLine(None, BasicInfoListener()).execute(TPath[numPath]) #プロダクションファイル内のメソッド名をすべて取得

        number = 0
        for ProductionMethod in Productionmethods_list:
            rd = rdict(testMethodMapcall)
            remethods = rd["^(?=.*" + ProductionMethod + ").*$"]
            if len(remethods) == 0:
                pass
            else:
                rts = list(set(remethods))
                for rt in rts:
                    startline = int(ProductionmethodLine_list[ProductionMethod][0])-1
                    endline = int(ProductionmethodLine_list[ProductionMethod][1])
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
                    db.testList.insert_one(post)  
                
                
                file = open('projects\\' + projects_key + '\\' + project_name + '\\main\\' + 'detectedcode_' + str(number) + '.java','w') # Nicad_3.javaのファイルを開く
                line_start = int(ProductionmethodLine_list[ProductionMethod][0])-1
                line_end = int(ProductionmethodLine_list[ProductionMethod][1])
                f = open(PPath[numPath], "r", encoding="utf-8")
                lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
                f.close()
                print('<Production Code>')
                for x in range(line_start,line_end):
                    srcLow = lines[x].replace('\n', '') + '\n'
                    print(srcLow)
                    file.write(srcLow)
    
                number += 1  


def makeFolder():
    os.mkdir('projects')
    projects_array = ['0123','ABCD','EFGH','IJKL','MNOP','QRST','UVW','XYZ']
    # projects_array = ['0123']
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
            # os.mkdir('projects\\' + project + '\\' + project_folder + '\\test')

def dict_projectName():
    projectName = defaultdict(list)
    projects_array = ['0123']
    for project in projects_array:
        data_set = glob.glob('D:\\ryosuke-ku\\data_set\\Git_20161108\\' + project + '\\*')
        for project_data in data_set:
            num_slash = project_data.rfind("\\")
            project_folder = project_data[num_slash + 1:]
            # print(project_folder)
            projectName[project].append(project_folder)
    
    return projectName

def delete_emptyProjects():
    try:
        os.rmdir('projects\\0123\\')
    except OSError as e:
        print('catch OSError:', e)
        pass


if __name__ == '__main__':
    # makeFolder()

    clint = MongoClient()
    db = clint['testList']

    projects_dic = dict_projectName()

    num_IndexError = 0
    num_UnicodeEncodeError = 0
    num_UnicodeDecodeError = 0
    num_RecursionError = 0
    num_FileNotFoundError = 0
    for projects_key in projects_dic:
        # print(projects_key)
        for projects_item in projects_dic[projects_key]:
            # print(projects_item)
            project_num = len(projects_item)
            # print(project_num)



            PPath = printProductionPath(projects_key + '\\' + projects_item)
            TPath = printTestPath(projects_key + '\\' + projects_item)
            if len(PPath) != 0 and len(TPath) != 0:
                # print(PPath)
                # print(TPath)
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
