import json

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