#导入pymongo
from pymongo import MongoClient
#建立连接
client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')
#获取数据库
db = client.xujunhao_db
db = client['xujunhao_db']
#获取一个集合
user_collection = db.user
user_collection = db['user']

collection = db.user

collection.find_one()
res = user_collection.find_one({"name":"xujunhao"})
print(res)
#collection.find() 
res = user_collection.find({"name":"xujunhao"})
for i in res:
  print(i)
#collection.find().count() 
num = user_collection.find({"name":"xujunhao"}).count()
print(num)