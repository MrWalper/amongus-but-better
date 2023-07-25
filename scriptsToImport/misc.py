import time
import json

def cooldown(lastActivated:int, cooldown:int):
    now = time.time()
    if now - lastActivated >= cooldown:
        return True
    else:
        return False
    
def openJson(path):
    with open(path, "r") as file:
        data = json.load(file)
        return(data)

def writeJson(path,itemToEdit,newData):
    with open(path, "w") as file:
        data = json.load(file)
        data[itemToEdit] = newData
        file.seek(0)
        json.dump(data, indent=4)
        file.truncate()