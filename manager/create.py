import json
from manager.todo_manager import Todo

file_name = "config.json"

def write_empty_object():
  with open(file_name, "w") as config:
    json.dump({}, config)

# if we have a exception where the json is empty and we read it the code crashes, to prevent the crash we write empty object to the json if its empty 
def check_for_empty():
  with open(file_name, "r") as config:
    if not config.read(): write_empty_object()

def create_file():
  try:
    with open(file_name, "x"): pass
    write_empty_object()
  except FileExistsError:
    check_for_empty()
  
def create_save(todo: Todo):
  create_file()
  
  # read and cache already loaded json so we can update it
  config_parsed: dict
  with open(file_name, "r") as config:
    config_parsed = json.load(config)
    
  # update logic
  config_parsed.update(todo.to_dict())
  with open(file_name, "w") as config:
    json.dump(config_parsed, config)
    
def main():
  user_input_name = input("input the name of the todo: ")
  user_input_desc = input("input the description of the todo: ")
  if not user_input_name or not user_input_desc: 
    print("failed the todo creation")
    return
  
  todo = Todo(user_input_name, user_input_desc)
  
  create_save(todo)