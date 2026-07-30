import json

FILE_NAME = "config.json"

def delete(todos: dict, target: str) -> dict:
    removed = todos.pop(target, None)
    
    if removed is not None:
        print(f"Successfully deleted task: '{target}'")
    else:
        print(f"Task '{target}' was not found")
        
    return todos

def update(todos: dict):
  with open("config.json", "w") as config:
    json.dump(todos, config)

def read_config(target: str):
  try: 
    with open("config.json", "r") as config: 
      config_parsed = json.load(config)
      clean_list = delete(config_parsed, target)
      update(clean_list)
  except FileNotFoundError:
      print("Config file doesn't exist yet Create a todo first!")
  except json.JSONDecodeError:
      print("Config file is empty or corrupted")
      print("Try deleting config.json or writing new todo if the json is empty")
    
def main():
  print("Name of the todo you want to delete")
  user_input_name = input("Input: ")
  if not user_input_name:
    print("invalid name input")
    return
  
  read_config(user_input_name)