from master import *
import sys

# sys.argv

m = Manipulation()

def mod(type, value):
    if type == "issue":
        m.addIssue(value)
        return()
    if type == "politician":
        m.addPolitician(value)
        return()
    else:
        print("Invalid type")
        return()

if __name__ == "__main__":
    mod(sys.argv[1], sys.argv[2])
