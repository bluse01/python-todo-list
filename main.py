from manager.create import main as create

print("todo app - python")
print("1. create new todo")
print("2. delete a task")

# using recursively func to get the valid user input
def getUserInput():
  try:
    return int(input("input: "))
  except ValueError:
    print("invalid input try again!")
    return getUserInput()

userInput = getUserInput()
match userInput:
  case 1:
    create()
  case 2:
    pass