import json
import fs
import random

"""
Files should be .json, and should be of this structure:

{
    "politicians": [],
    "issues": []

}

Use the following for testing:

from master import *
m = Manipulation()
m.addIssue("Climate Change", "data.json")

from master import *
g = Get()
g.pullRandomPair()
"""
class Manipulation:
    def addPolitician(self,n,file="data.json"): #adds a politician n into file file
        with open(file, "r") as f:
            data = json.load(f)
        f.close()
        with open(file,"w") as f:
            data['politicians'].append(n)
            f.write(json.dumps(data,indent=1))
            print("Successfully added '" + n + "' to the list of politicians. Total politicians in file: " + str(len(data['politicians'])))
        f.close()

    def addIssue(self,n,file="data.json"): #adds a politician n into file file
        with open(file, "r") as f:
            data = json.load(f)
        f.close()
        with open(file,"w") as f:
            data['issues'].append(n)
            f.write(json.dumps(data,indent=1))
            print("Successfully added '" + n + "' to the list of issues. Total issues in file: " + str(len(data['issues'])))
        f.close()

class Get:
    def grab(self, file="data.json"):
        with open(file,"r") as f:
            return(json.load(f))
        close()

    def pullRandomPair(self,file="data.json"):
        grab = Get.grab(self)
        data = grab
        politician  = random.choice(data['politicians'])
        issue = random.choice(data['issues'])
        print(politician,issue)
