import json
from datetime import datetime
from datetime import date
import io


with open("Members.json", "r") as members, open("Members_Copy.json", "w") as Members_Copy:
    Members_Copy.write(members.read())
    print("Copy Created successfully")

with open('Members_Copy.json', 'w') as newFile:
    data = json.load(newFile)
    data["Age"] = "134" # <--- add `id` value.
    newFile.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, newFile, indent=4)
    newFile.truncate()     # remove remaining part
