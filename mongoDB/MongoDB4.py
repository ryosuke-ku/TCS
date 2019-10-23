from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

class testListMongo(object):

    def __init__(self):
        self.clint = MongoClient()
        self.db = self.clint['newDataBase']

    def add_one(self):
        """データ挿入"""
        post = {
            'title': 'ハリネズミ',
            'content': 'ハリネズミ可愛い~',
            'created_at': datetime.now()
        }
        return self.db.testList.insert_one(post)

    def get_one(self):
        return self.db.testList.find_one()

    def get_all(self):
        return self.db.testList.find()

    def get_from_line(self,startline1,endline1):
        return self.db.testList.find({'startline1':startline1,'endline1':endline1})

    def get_from_oid(self,oid):
        return self.db.testList.find_one({'_id':ObjectId(oid)})

def main():
    obj = testListMongo()
    rest = obj.get_all()
    # for i in rest:
    #     print(i)
    # print(rest)
    num1 = '6'
    num2 = '19'
    items = obj.get_from_line(num1,num2)
    for item in items:
        print(item)



if __name__ == '__main__':
    main()