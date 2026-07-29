import json

fileName = "config.json"

def writeEmptyObject():
  with open(fileName, "w") as config:
    json.dump({}, config)

# if we have a exception where the json is empty and we read it the code crashes, to prevent the crash we write empty object to the json if its empty 
def checkForEmpty():
  with open(fileName, "r") as config:
    if not config.read(): writeEmptyObject()

def createFile():
  try:
    with open(fileName, "x"): pass
    writeEmptyObject()
  except FileExistsError:
    checkForEmpty()
  
def createSave(todo):
  createFile()
  
  # read and cache already loaded json so we can update it
  configParsed: dict
  with open(fileName, "r") as config:
    configParsed = json.load(config)
    
  # update logic
  configParsed.update(todo)
  with open(fileName, "w") as config:
    json.dump(configParsed, config)
    
def main():
  userInputName = input("input the name of the todo: ")
  userInputDesc = input("input the description of the todo: ")
  if not userInputName or not userInputDesc: 
    print("failed the todo creation")
    return
  
  createSave({userInputName: userInputDesc})