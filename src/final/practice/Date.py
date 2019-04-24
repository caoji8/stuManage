import json
#写数据
def saveDate(date,filename = "user.json"):
    with open(filename,mode="w",encoding="utf-8") as sa:
        json.dump(date,sa)
#读数据
def loadDate(filename="user.json"):
    with open(filename,mode='r',encoding='utf-8') as op:
        user_load = json.load(op)
        return user_load
