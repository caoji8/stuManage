import json
def saveDate(date,filename = "user.json"):
    with open(filename,mode="w",encoding="utf-8") as f:
        json.dump(date,f)
saveDate("hello")