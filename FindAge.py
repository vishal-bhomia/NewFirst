import json
from datetime import date
from datetime import datetime
gargertg
i=0
#function to calculate age when DOB is provided
def calculate_age(DOB):
    today = date.today()
    return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

#loading existiong JSON into an object jsonObj
copy = open("Members.json","r")
memData = copy.read()
jsonObj = json.loads(memData)

#creating a JSON file and populating it with existing JSON appended with AGE
with open('Members_Copy.json', 'w') as newFile:
    while(i < len(jsonObj)):
        jsonObj[i]["Age"] = calculate_age(datetime.strptime(jsonObj[i]["DOB"], '%Y-%m-%d'))
        i += 1
    json.dump(jsonObj, newFile, indent=4)
print("Completed")
print("Result file created with a name ""Members_Copy.json"", please check the original folder")