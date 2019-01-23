import json
from datetime import date
from datetime import datetime


def calculate_age(DOB):
    today = date.today()
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))



copy = open("Members.json","r")
memData = copy.read()
jsonObj = json.loads(memData)

i=0
with open('Members_Copy.json', 'w') as newFile:
    while(i < len(jsonObj)):
        jsonObj[i]["Age"] = calculate_age(datetime.strptime(jsonObj[i]["DOB"], '%Y-%m-%d'))
        #print(jsonObj[i])
        i += 1
    json.dump(jsonObj, newFile, indent=4)
print("Result file created")