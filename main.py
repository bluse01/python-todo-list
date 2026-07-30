from manager.create import main as create
from manager.delete import main as delete

print("todo app - python")
print("1. create new todo")
print("2. delete a task")

# using recursively func to get the valid user input
def get_user_input():
  try:
    return int(input("input: "))
  except ValueError:
    print("invalid input try again!")
    return get_user_input()

user_input = get_user_input()
match user_input:
  case 1:
    create()
  case 2:
    delete()